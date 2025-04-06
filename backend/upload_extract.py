import asyncio
from dotenv import load_dotenv
load_dotenv()

import time
import boto3

s3 = boto3.client("s3")
textract = boto3.client("textract")

S3_BUCKET_NAME = 'insurance-plans-pdfs'

# UPLOAD FILES TO S3 BUCKET
def upload_to_s3(file, bucket: str, key: str):
    s3.upload_fileobj(file.file, bucket, key)
    return key

# START TEXTRACT
def start_textract_job(bucket: str, key: str) -> str:
    response = textract.start_document_text_detection(
        DocumentLocation={"S3Object": {"Bucket": bucket, "Name": key}}
    )
    return response["JobId"]

# GET TEXTRACT RESULTS
def get_textract_result(job_id: str) -> str:
    while True:
        response = textract.get_document_text_detection(JobId=job_id)
        status = response["JobStatus"]
        if status in ["SUCCEEDED", "FAILED"]:
            break
        time.sleep(2)

    if status == "FAILED":
        raise Exception("Textract job failed")

    lines = [
        block["Text"]
        for block in response["Blocks"]
        if block["BlockType"] == "LINE"
    ]
    return "\n".join(lines)

async def process_file(file):
    # Upload to S3
    await asyncio.to_thread(upload_to_s3, file, S3_BUCKET_NAME, file.filename)
    # Start Textract job and get job_id
    job_id = await asyncio.to_thread(start_textract_job, S3_BUCKET_NAME, file.filename)
    # Get Textract result
    result = await asyncio.to_thread(get_textract_result, job_id)
    return {
        "name": file.filename,
        "text": result
    }

async def upload_and_extract(files):
    tasks = [process_file(file) for file in files]
    return await asyncio.gather(*tasks)