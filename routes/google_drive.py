from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from fastapi import UploadFile

def authenticate_google_drive(credentials_file: str):
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=['https://www.googleapis.com/auth/drive.file']
    )
    return build('drive', 'v3', credentials=credentials)


def upload_image_to_google_drive(upload_file: UploadFile, service) -> str:
    file_metadata = {
        'name': upload_file.filename,  
        'mimeType': upload_file.content_type 
    }


    media = MediaIoBaseUpload(upload_file.file, mimetype=upload_file.content_type)

  
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    return f"https://drive.google.com/uc?id={file.get('id')}"