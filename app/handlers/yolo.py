from ultralytics import YOLO
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run(file_path):
    logging.debug(f'running yolo on file {file_path}')
