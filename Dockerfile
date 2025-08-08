# Use an official Redis as the base image
FROM redis:latest

# Expose the default port for Redis (6379)
EXPOSE 6379

# Command to run the Redis server
CMD ["redis-server"]

# Use python:3.9.18 as the base image
FROM python:3.9.18

# Set the working directory in the container
WORKDIR /usr/src/sonic_engine

# Copy the current directory contents into the container at /usr/src/sonic_engine
COPY . /usr/src/sonic_engine/

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

# Install the sonic_engine package from the local directory
RUN pip install /usr/src/sonic_engine/

# Clone the sonic_engine_templates repository
RUN git clone https://github.com/AhmedCoolProjects/sonic_engine_templates.git templates

# Set the working directory to hello_world inside the templates directory
WORKDIR /usr/src/sonic_engine/templates/hello_world/

# Command to run the Python application
CMD ["python", "app.py"]
