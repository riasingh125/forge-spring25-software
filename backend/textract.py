import boto3
import time

textract = boto3.client("textract")


def start_textract_job(bucket: str, key: str) -> str:
    response = textract.start_document_text_detection(
        DocumentLocation={"S3Object": {"Bucket": bucket, "Name": key}}
    )
    return response["JobId"]

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
