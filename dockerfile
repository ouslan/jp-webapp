FROM rust:alpine3.20 AS rust_builder

# Install cmake
RUN apk add --no-cache cmake

# Rest of your Rust builder stage

FROM python:3.12

# Install gcc
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ && rm -rf /var/lib/apt/lists/*

# Copy the built Rust artifacts from the Rust builder stage
COPY --from=rust_builder /usr/local/cargo /usr/local/cargo

# Set the cargo/bin directory in the PATH
ENV PATH="/usr/local/cargo/bin:${PATH}"

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
