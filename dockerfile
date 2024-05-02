FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8000

# Copy the rest of the application code
COPY . .