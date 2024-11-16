#!/bin/bash

# Get the absolute path of the current script's directory
PROJECT_DIR=$(cd "$(dirname "$0")" && pwd)
UPLOADS_DIR="$PROJECT_DIR/app/uploads"

# Ensure the uploads directory exists
mkdir -p "$UPLOADS_DIR"

# Paths to files to update
ODM_HANDLER_FILE="$PROJECT_DIR/app/odm_handler.py"
DOCKER_COMPOSE_FILE="$PROJECT_DIR/docker-compose.yml"

# Function to perform first-time setup
first_time_setup() {
    echo "Performing first-time setup..."

    # Replace specific paths in odm_handler.py
    echo "Updating $ODM_HANDLER_FILE with placeholder path 'x'..."
    sed -i.bak "s|'/Users/arshia/classifytheworld/app/uploads/datasets'|'$UPLOADS_DIR/datasets'|" "$ODM_HANDLER_FILE"

    # Replace specific paths in docker-compose.yml
    echo "Updating $DOCKER_COMPOSE_FILE with placeholder path 'x'..."
    sed -i.bak "s|/Users/arshia/classifytheworld/app/uploads|$UPLOADS_DIR|" "$DOCKER_COMPOSE_FILE"

    echo "First-time setup complete. You can now run recurring builds."
}

# Function to rebuild and run Docker containers
rebuild_and_run() {
    echo "Building and starting Docker containers..."
    docker-compose down
    docker-compose up --build
}

# Main menu
echo "Select an option:"
echo "1. First-time setup (replace paths and build)"
echo "2. Recurring usage (just rebuild the container)"
read -p "Enter your choice [1-2]: " choice

case $choice in
    1)
        first_time_setup
        rebuild_and_run
        ;;
    2)
        rebuild_and_run
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac
