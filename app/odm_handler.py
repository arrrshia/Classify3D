import subprocess
import os
import logging
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG
logger = logging.getLogger(__name__)
def run_odm(upload_folder):
    output_folder = os.path.join(upload_folder, 'output')
    os.makedirs(output_folder, exist_ok=True)

    docker_cmd = [
        'docker', 'run', '-i', '--rm',
        '-v', f'/Users/arshia/classifytheworld/app/uploads/datasets:/datasets',
        'opendronemap/odm', '--project-path', '/datasets', 'project'
    ]

    logging.debug(f"Running Docker command: {' '.join(docker_cmd)}")  # Debug log

    try:
        process = subprocess.run(
            docker_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Ensures output is readable
        )
        print(f"Docker stdout: {process.stdout}")  # Debug the Docker output
        print(f"Docker stderr: {process.stderr}")  # Debug the Docker error output

        if process.returncode != 0:
            raise Exception(f"ODM processing failed: {process.stderr}")
    except FileNotFoundError:
        raise Exception("Docker not found. Ensure Docker is installed and /var/run/docker.sock is accessible.")
    except Exception as e:
        raise Exception(f"Error during ODM processing: {e}")
