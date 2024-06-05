from base64 import b64encode
import time
import os

def get_image_base64(image_path: str):
    with open(image_path, 'rb') as img_file:
        return b64encode(img_file.read()).decode('utf-8')

def generate_unique_filename():
    timestamp = int(time.time())
    return f'tree_{timestamp}.png'

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)