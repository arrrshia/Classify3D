import os
import shutil
import logging
import subprocess
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG
logger = logging.getLogger(__name__)

load_dotenv()

def run(upload_folder):
    output_folder = os.path.join(upload_folder, 'output')
    local_project_dir = os.getenv('LOCAL_PROJECT_DIR')
    os.makedirs(output_folder, exist_ok=True)

    docker_cmd = [
        'docker', 'run', '-i', '--rm',
        '-v', f'{local_project_dir}/app/uploads/datasets:/datasets',
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
        logging.debug(f"Docker stdout: {process.stdout}")  # Debug the Docker output
        logging.debug(f"Docker stderr: {process.stderr}")  # Debug the Docker error output

        if process.returncode != 0:
            raise Exception(f"ODM processing failed: {process.stderr}")
    except FileNotFoundError as f:
        logging.debug(f)
        raise Exception("Docker not found. Ensure Docker is installed and /var/run/docker.sock is accessible.")
    except Exception as e:
        raise Exception(f"Error during ODM processing: {e}")
