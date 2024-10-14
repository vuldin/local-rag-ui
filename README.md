This repo shows how you can set up a RAG pipeline with locally-hosted, open LLMs! This assumes you have an IDE to run jupyter notebooks, and are comfortable using your terminal.
This works on a Macbook that has an M2 processor. YMMV depending on your machine and OS. 

The chatbot is an expert in potty training. This may seem silly to those who have never potty trained a small child, but as a first time parent, I would have loved a helpful chatbot on this topic!

**Prerequisites:**

Make sure to create an **environment** (conda or virtualenv work well). Install everything in requirements.txt: 'pip install -r requirements.txt', then activate the environment in your shell.

To install **ollama** and download the llm and embedding models, visit https://ollama.com/

To start ollama: 'ollama start'

To install and run **qdrant** locally, visit https://qdrant.tech/documentation/quickstart/

To start qdrant:
Make sure to install **Docker** if you haven't already.

'docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant'

To check if it's running:
navigate to localhost:6333/dashboard in a browser

To generate the **data**:
Run test_servers.ipynb to create your Qdrant collection and verify that your models and vector store are working.

To start **FastAPI**:
'uvicorn server:app --host 0.0.0.0 --port 8000'

To check if it's running:
Go to http://localhost:8000/docs

And send a test query:
'curl -X POST "http://localhost:8000/invoke" -H "Content-Type: application/json" -d '{"input": {"query": "Your question here"}}''

Or, for streaming:
'curl -X POST "http://localhost:8000/stream" -H "Content-Type: application/json" -d '{"input": {"query": "Your question here"}}''

To run **Streamlit** as a simple test app:
Make sure all the stuff above is running.
In your shell, do 'streamlit run streamlit_app.py' and interact with the chatbot via the browser!

