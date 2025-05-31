import boto3
import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('AWS_ACCESS_KEY'))
print(os.getenv('AWS_SECRET_ACCESS_KEY'))

app = FastAPI()

class Job(BaseModel):
    task_type: str
    payload: dict


sqs_client = boto3.client(
    'sqs',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

QUEUE_URL = os.getenv('SQS_QUEUE_URL')


@app.post("/submit-job")
def submit_job(job: Job):
    """
    Endpoint to submit a job with a task type and payload.
    """
    # Here you would typically add the job to a queue or process it
    response = sqs_client.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=job.json()
    )
    return {"message": "Job submitted successfully", "job_id": response.get('MessageId')}

