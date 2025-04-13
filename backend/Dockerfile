# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy your application code into container
COPY . .

# Expose port (e.g., 5000)
EXPOSE 5000

# Command to run your application
CMD ["python", "app.py"]
