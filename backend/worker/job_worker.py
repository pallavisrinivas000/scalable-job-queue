import boto3
import os
import json
import time
import logging
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)



sqs_client = boto3.client(
    'sqs',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
QUEUE_URL = os.getenv('SQS_QUEUE_URL')

def process_job(job):
    logger.info("provessing job:", job)

    logger.info(json.dumps(job, indent=2))
    time.sleep(2)  # Simulate job processing time


def poll_queue():
    logger.info("Polling SQS queue for new jobs...")
    while True:
        response = sqs_client.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20
        )
        messages = response.get('Messages', [])

        if not messages:
            logger.info("No new messages in the queue.")
            continue

        for message in messages:
            try: 
                job = json.loads(message['Body'])
                process_job(job)

                # Delete the message from the queue after processing
                sqs_client.delete_message(
                    QueueUrl=QUEUE_URL,
                    ReceiptHandle=message['ReceiptHandle']
                )
                logger.info("Job processed and message deleted from queue.")
            except Exception as e:
                logger.warning(f"Error processing job: {e}")
                # Optionally, you could log the error or send it to a dead-letter queue
                continue
        logger.info("Waiting for new messages...")
if __name__ == "__main__":
    poll_queue()
