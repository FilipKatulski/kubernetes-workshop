# Set the base image
FROM pytorch/pytorch:latest

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
# Install additional dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt
    # pip install --no-cache-dir -r requirements.txt 

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . .

# Set the default command to run when the container starts
CMD ["python", "app.py"]
