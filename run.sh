#!/bin/bash

mkdir -p /app/uploads

echo "Building and starting Docker containers..."

docker-compose down
docker-compose up --build
