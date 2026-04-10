# Base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run app
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
