from operator import itemgetter
from typing import Any

from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from langserve import add_routes

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore



app = FastAPI()

# llm
model = "llama3.2:1b"
llm = OllamaLLM(model=model)

# prompt
RAG_PROMPT_TEMPLATE = """\
<|start_header_id|>system<|end_header_id|>
You are a helpful potty training assistant. You answer user questions based on context. If you can't answer the question with the context, say you don't know.
Context:
{context}
<|eot_id|>

<|start_header_id|>user<|end_header_id|>
User Question:
{query}
<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>
"""
rag_prompt = PromptTemplate.from_template(RAG_PROMPT_TEMPLATE)

# vector store
url="http://localhost:6333"
collection_name="PottyTraining"

embeddings = OllamaEmbeddings(
    model="mxbai-embed-large",
)
qdrant_vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name=collection_name,
    prefer_grpc=True,
    url=url
)

# retriever
retriever = qdrant_vector_store.as_retriever(
    search_type="mmr",  
    search_kwargs={"k": 3}    
)

# rag chain
lcel_rag_chain = {"context": itemgetter("query") | retriever, "query": itemgetter("query")}| rag_prompt | llm

class Input(BaseModel):
    query: str

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(
    app, 
    lcel_rag_chain.with_types(input_type=Input, output_type=str).with_config(
        {"run_name" : "PottyTraining_RAG"}
    )
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
