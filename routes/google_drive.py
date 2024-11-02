from fastapi import UploadFile
import os
import shutil

STATIC_DIR = "static/images"
os.makedirs(STATIC_DIR, exist_ok=True)

def upload_image_to_tmp(image_data, image_name) -> str:
    logo_path = os.path.join(STATIC_DIR, image_name)
    with open(logo_path, "wb") as f:
        f.write(image_data)
    return f"/static/images/{image_name}"