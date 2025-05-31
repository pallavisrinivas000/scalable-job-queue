 Scalable Job Queue System
A production-ready, containerized job queue system using FastAPI, AWS SQS, Podman/Docker, and GitHub Actions for CI/CD. Designed to decouple job submission (API) from job processing (Worker) using a message queue pattern.

🧩 Project Structure
.
├── README.md
├── backend
│   ├── Dockerfile               # Dockerfile for FastAPI app
│   ├── Dockerfile.worker        # Dockerfile for job worker
│   ├── app/
│   │   └── main.py              # FastAPI app
│   ├── worker/
│   │   └── job_worker.py        # Worker consuming from SQS
│   ├── poetry.lock              # Poetry lockfile
│   └── pyproject.toml           # Project dependencies
├── docker-compose.yml          # Local dev orchestration
└── .github/workflows/          # CI/CD workflows


🌐 Features

API (FastAPI): Accepts job submissions via /submit-job endpoint.

Worker (Python): Listens to SQS, processes jobs.

AWS SQS: Handles message queueing between API and worker.

Containerized: Build and run with Podman or Docker.

GitHub Actions CI/CD: Automates build and deployment to AWS ECR.

Secure: Uses GitHub secrets for AWS credentials.

⚙️ Technologies Used
FastAPI – for building the job submission API

Python 3.11 – runtime environment

Boto3 – AWS SDK for interacting with SQS

AWS SQS – decoupled message queue

AWS ECR – container registry

Poetry – dependency management

Podman / Docker – containerization

GitHub Actions – continuous integration and deployment

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/your-username/scalable-job-queue.git
cd scalable-job-queue
2. Set Up Environment Variables
Create a .env file inside backend/ with the following:
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
SQS_QUEUE_URL=https://sqs.<region>.amazonaws.com/<account_id>/<queue_name>
3. Run Locally (with Docker Compose)
cd backend
podman-compose up --build
This will start:

job-queue-api on port 8000

job-queue-worker running in background

🧪 API Usage
Submit Job
bash
Copy
Edit
curl -X POST http://localhost:8000/submit-job \
  -H "Content-Type: application/json" \
  -d '{
    "task_type": "email",
    "payload": {
      "to": "test@example.com",
      "subject": "Hello"
    }
  }'
Expected Response
json
Copy
Edit
{
  "message": "Job submitted successfully",
  "job_id": "e.g. 1c7a4e5a-..."
}
🛠️ GitHub Actions CI/CD
CI Workflow: Runs tests, builds images, and pushes to AWS ECR on every push to master.

Deploy Workflow: Pushes updated API and Worker images to ECR.

GitHub Secrets needed:

AWS_ACCESS_KEY

AWS_SECRET_ACCESS_KEY

AWS_REGION

SQS_QUEUE_URL

🐳 Building Manually
Build and Run API
bash
Copy
Edit
cd backend
podman build -f Dockerfile -t job-queue-api .
podman run -p 8000:8000 job-queue-api
Build and Run Worker
bash
Copy
Edit
cd backend
podman build -f Dockerfile.worker -t job-queue-worker .
podman run job-queue-worker
📦 Deployment
Pushed Docker images are stored in Amazon ECR

You can deploy them to ECS, EC2, Kubernetes, or other cloud runtimes

✅ TODOs
 Add retry & dead-letter queue logic

 Unit tests for API and Worker

 Add support for task types and handlers

 ECS deployment with Terraform or CDK