FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pydantic openai fastapi uvicorn
EXPOSE 7860
# CRITICAL: Change this from 'python -m http.server' to:
CMD ["python", "env_server.py"]
