FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN apt-get update && \
    apt-get install -y curl git supervisor && \
    rm -rf /var/lib/apt/lists/*
#RUN pip install --no-cache-dir pipenv && pipenv install
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir "fastapi[standard]"
#COPY *.py .
#CMD [ "python", "./app.py" ]
EXPOSE 8000 8501
#CMD ["python", "app.py"]
#RUN fastapi dev server.py &
#CMD ["streamlit", "run", "streamlit_app.py"]
# Copy the Supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# Start Supervisor, which manages both FastAPI and Streamlit
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
