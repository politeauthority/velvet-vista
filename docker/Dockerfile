# Set the Docker registry URL
ARG DOCKER_REGISTRY="docker.io/library"

# Use the official Python 3.10 image with Alpine 3.16 as the base image
FROM ${DOCKER_REGISTRY}/python:3.10-alpine3.16 as base

# Set the working directory to /app
WORKDIR /app

# Copy the local src directory to the working directory in the container
ADD ./src /app

# Install apk requirements
RUN apk add --update --no-cache --virtual .build-deps \
    gcc libc-dev linux-headers bash git \
    && apk add --no-cache libffi-dev \
    && apk add --no-cache --update --virtual .runtime-deps \
    libgcc libstdc++ ca-certificates \
    # Install Python dependencies
    && pip3 install --no-cache-dir -r /app/requirements.txt \
    # Remove build dependencies
    && apk del .build-deps

# App configuration
RUN mkdir /configs
ADD scripts/velvet-vista-build /bin/velvet-vista-build

# Dev Tools
RUN pip3 install --no-cache-dir -r /app/requirements-dev.txt
