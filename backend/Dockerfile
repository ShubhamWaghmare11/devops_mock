FROM python:3.9-slim

WORKDIR /app

# Copy and install dependencies first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

EXPOSE 8000

# Run the FastAPI app with Uvicorn, listening on all interfaces
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


