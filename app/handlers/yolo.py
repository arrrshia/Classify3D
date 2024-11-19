from ultralytics import YOLO
import os
import logging

logging.basicConfig(level=logging.INFO)

def run(image_path):
    logging.info(f'running yolo on file {image_path}')
    
    weights = os.path.join(os.path.dirname(__file__), 'weights.pt')

    return YOLO(weights)(image_path)
