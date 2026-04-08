FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 7860
# This runs a dummy server to keep the HF Space 'Running'
CMD ["python", "-m", "http.server", "7860"]
