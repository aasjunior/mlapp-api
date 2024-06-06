from base64 import b64encode
from datetime import datetime
import time
import os

def get_image_base64(image_path: str):
    with open(image_path, 'rb') as img_file:
        return b64encode(img_file.read()).decode('utf-8')

def generate_unique_filename(prefix: str):
    timestamp = int(time.time())
    return f'{prefix}_{timestamp}.png'

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def generate_log(error, traceback_details):
    with open('assets/log/error_log.txt', 'w') as file:
        file.write(f'[{current_time()}] Ocorreu um erro:\n{error}\n')
        file.write(traceback_details)  