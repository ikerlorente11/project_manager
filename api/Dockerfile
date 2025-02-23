# Use the official Python 3.9 image based on Alpine Linux for a lightweight container
FROM python:3.9-alpine

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from the host to the container
COPY requirements.txt requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire application code from the host to the container
COPY . .

# Expose port 8000 to allow external access to the application
EXPOSE 8000

# Set the default command to run when the container starts
# This script waits for the database to be ready before starting the application
CMD ["sh", "/app/wait-for-db.sh"]