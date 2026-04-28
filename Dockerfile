FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV and other packages
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the application files
COPY . .

# Expose port 7860 (Hugging Face Spaces standard port)
EXPOSE 7860

# Initialize the database
RUN python init_db.py

# Grant permissions to all files so the app can write to the database and upload images
RUN chmod -R 777 /app

# Start the Flask app using Gunicorn on port 7860
CMD ["gunicorn", "App:app", "-b", "0.0.0.0:7860"]
