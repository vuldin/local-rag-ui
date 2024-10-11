Prerequisites:
To install ollama and models, visit https://ollama.com/
To install and run qdrant locally, visit https://qdrant.tech/documentation/quickstart/

To start qdrant:
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant

To check if it's running:
navigate to localhost:6333/dashboard in a browser
