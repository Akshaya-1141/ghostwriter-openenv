FROM python:3.10-slim
WORKDIR /app

# Install dependencies directly
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir pydantic openai fastapi uvicorn openenv-core

# Copy all files
COPY . .

# EXPOSE the required port
EXPOSE 7860

# RUN the module directly without installing the package
CMD ["python", "-m", "server.app"]
