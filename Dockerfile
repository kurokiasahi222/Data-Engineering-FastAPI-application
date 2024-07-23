# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory
WORKDIR /src

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Command to run the FastAPI application
CMD ["fastapi", "run", "server.py"]
