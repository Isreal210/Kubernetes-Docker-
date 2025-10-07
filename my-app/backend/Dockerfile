# Use Python base image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

CMD ["python", "app.py"]
