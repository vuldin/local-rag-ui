This repo shows how you can set up a RAG pipeline with locally-hosted, open LLMs.

The chatbot is an expert in potty training. This may seem silly to those who have never potty trained a small child, but as a first time parent, I would have loved a helpful chatbot on this topic!

**Prerequisites:**

Make sure to create an **environment** (conda or virtualenv work well). Install everything in requirements.txt: 'pip install -r requirements.txt', then activate the environment in your shell.

To install **ollama** and models, visit https://ollama.com/

To start ollama: 'ollama start'

To install and run qdrant locally, visit https://qdrant.tech/documentation/quickstart/

To start **qdrant**:
'docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant'

To check if it's running:
navigate to localhost:6333/dashboard in a browser

To start **FastAPI**:
'uvicorn server:app --host 0.0.0.0 --port 8000'

To check if it's running:
Go to http://localhost:8000/docs

And send a test query:
'curl -X POST "http://localhost:8000/invoke" -H "Content-Type: application/json" -d '{"input": {"query": "Your question here"}}''

Or, for streaming:
'curl -X POST "http://localhost:8000/stream" -H "Content-Type: application/json" -d '{"input": {"query": "Your question here"}}''

To run a test app with a very simple interactive **Streamlit** experience:
Make sure all the stuff above is running.
In your shell, do 'streamlit run streamlit_app.py' and interact with the chatbot via the browser!

