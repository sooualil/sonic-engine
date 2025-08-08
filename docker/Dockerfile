FROM python:3.9.18

# Install redis-server
RUN apt-get update && apt-get install -y redis-server
# Remove cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt/*

# Copy the current directory contents into the container at /usr/src/sonic_engine
COPY . /usr/src/sonic_engine/

# Set the working directory in the container
WORKDIR /usr/src/sonic_engine

# Copy redis configuration file
COPY ./docker/redis.conf /etc/redis/redis.conf

# Copy entrypoint script
COPY ./docker/entrypoint.sh /usr/local/bin/entrypoint.sh

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the sonic_engine package from the local directory
RUN pip install --no-cache-dir .

# Clone the sonic_engine_templates repository
RUN git clone https://github.com/AhmedCoolProjects/sonic_engine_templates.git templates

# Set the working directory to hello_world inside the templates directory
WORKDIR /usr/src/sonic_engine/templates/hello_world/

# Run the entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
