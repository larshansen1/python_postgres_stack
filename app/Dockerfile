# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Define environment variable for Flask to be production-ready
ENV FLASK_APP=main.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]

