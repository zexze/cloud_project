# Use a base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy files into the container
COPY model.pkl ./model.pkl
COPY app.py ./app.py
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
