
# Handles Uploading PDFs to Amazon s3

# pip install boto3

import boto3
from dotenv import load_dotenv
load_dotenv()

s3 = boto3.client("s3")

def upload_to_s3(file, bucket: str, key: str):
    s3.upload_fileobj(file.file, bucket, key)
    return key