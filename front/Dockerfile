# Use a base image of Node.js
FROM node:23-alpine

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install the dependencies specified in package.json
RUN npm install

# Copy all project files from the host to the container
COPY . .

# Expose the port on which the application will run
EXPOSE 3000

# Execute the startup script when the container starts
CMD ["sh", "/app/startup.sh"]