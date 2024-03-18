
# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the current directory into the container
COPY . .

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Replace the hub_url in the configuration file
RUN sed -i 's|http://localhost:4444/wd/hub|http://selenium-hub:4444/wd/hub|g' /app/config.json