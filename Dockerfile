FROM python:3.10-slim

WORKDIR /app

# Copy all files into the container
COPY . .

# Install the project and dependencies in editable mode or as a package
RUN pip install --no-cache-dir .

# Expose the mandatory Hugging Face port
EXPOSE 7860

# Run the server module using the python -m syntax
CMD ["python", "-m", "server.app"]
