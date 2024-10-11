This repo shows how you can set up a RAG pipeline with locally-hosted, open LLMs!

The chatbot is an expert in potty training. 

**Prerequisites:**

To install ollama and models, visit https://ollama.com/

To install and run qdrant locally, visit https://qdrant.tech/documentation/quickstart/

To start qdrant:
`$ docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant`

To check if it's running:
navigate to localhost:6333/dashboard in a browser

Before running the notebook, create an environment -- for example:
`$ virtualenv mypottytrainingchatbot`

Activate your environment and install the requirements:
`$ source mypottytrainingchatbot/bin/activate`
`$ pip install -r requirements.txt`

Make sure your IDE, such as Visual Studio, is running the virtual environment (select it as your kernel)



