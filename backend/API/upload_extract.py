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
	# Wait for the job to finish
	while True:
		response = textract.get_document_text_detection(JobId=job_id)
		status = response["JobStatus"]
		if status in ["SUCCEEDED", "FAILED"]:
			break
		time.sleep(1)  # Optional: Add a delay to avoid excessive polling
	if status == "FAILED":
		raise Exception("Textract job failed")
	# Initialize a list to accumulate lines and handle pagination
	all_lines = []
	# Process the first batch
	lines = [
		block["Text"]
		for block in response["Blocks"]
		if block["BlockType"] == "LINE"
	]
	all_lines.extend(lines)
	# Check for pagination
	next_token = response.get("NextToken")
	while next_token:
		response = textract.get_document_text_detection(JobId=job_id,
														NextToken=next_token)
		lines = [
			block["Text"]
			for block in response["Blocks"]
			if block["BlockType"] == "LINE"
		]
		all_lines.extend(lines)
		next_token = response.get("NextToken")
	return "\n".join(all_lines)


async def upload_and_extract(files: dict):
	job_map = {}
	upload_jobs = []
	# start all s3 jobs and wait till they finish
	for file, premium in files.items():
		job_map[file.filename] = premium
		job = asyncio.to_thread(upload_to_s3, file, S3_BUCKET_NAME,
								file.filename);
		upload_jobs.append(job)
	await asyncio.gather(*upload_jobs)

	textract_jobs = {}
	for file, premium in files.items():
		job_id = await asyncio.to_thread(start_textract_job, S3_BUCKET_NAME,
										 file.filename)
		textract_jobs[file.filename] = (job_id, premium)

	results = {}
	for filename, (job_id, premium) in textract_jobs.items():
		result = await asyncio.to_thread(get_textract_result, job_id)
		results[filename] = [result, premium]
	return results
