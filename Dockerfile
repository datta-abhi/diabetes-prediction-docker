FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Start both FastAPI and Streamlit
CMD ["sh", "-c", "uvicorn api_app:app --host 0.0.0.0 --port 8000 & streamlit run ui_app.py --server.port 8501 --server.enableCORS false"]