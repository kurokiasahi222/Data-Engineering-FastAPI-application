# Use the official Python image from the Docker Hub
FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the code into the container
COPY . /app

# # # make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Run the app
CMD ["/app/entrypoint.sh"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]


# # Copy the requirements file into the container
# COPY requirements.txt .
# # Copy the rest of the code into the container
# COPY . .

# # Set the working directory
# WORKDIR /app/

# # default installs
# RUN apt-get update && \
#     apt-get install -y \
#     build-essential \
#     python3-dev \
#     python3-setuptools \
#     gcc \
#     make

# # Create a virtualenv
# RUN python-3 -m venv /opt/venv && \
#     /opt/venv/bin/python -m pip instal pip --upgrade  && \ 
#     /opt/venv/bin/python -m pip instal -r requirements.tet

# # purge unused
# RUN apt-get remove -y --purge make gcc build-essential \
#     && apt-get autoremove -y \
#     && rm -rf /var/lib/apt/lists/*

# # # Install dependencies
# # RUN pip install --no-cache-dir -r requirements.txt

# # # make entrypoint executable
# # RUN chmod +x ./src/entrypoint.sh

# # run the app
# # Command to run the FastAPI application
# # CMD ["fastapi", "run", "server.py"]
