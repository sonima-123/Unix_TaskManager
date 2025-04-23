# Use official Python 3.13.3 base image
FROM python:3.13.3

# Set working directory
WORKDIR /app

# Copy requirements first for caching benefits
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY app/ ./app/
COPY .env .

# Expose the default Uvicorn port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]