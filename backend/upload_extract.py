import asyncio
from dotenv import load_dotenv
load_dotenv()

from s3_upload import upload_to_s3
from textract import start_textract_job, get_textract_result


async def upload_and_extract(files):
    results = []
    # upload pdf to s3
    for file in files:
        await asyncio.to_thread(upload_to_s3,file, 'insurance-plans-pdfs', file.filename)
        job_id = await asyncio.to_thread(start_textract_job,'insurance-plans-pdfs', file.filename)
        result = await asyncio.to_thread(get_textract_result,job_id)
        results.append(result)
    return results