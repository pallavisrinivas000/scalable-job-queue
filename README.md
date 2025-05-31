# 🚀 Scalable Job Queue System

A production-ready, containerized **job queue system** using **FastAPI**, **AWS SQS**, **Podman/Docker**, and **GitHub Actions** for CI/CD. Designed to decouple job submission (API) from job processing (Worker) using a message queue pattern.

---

## 🧩 Project Structure

```
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
```

---

## 🌐 Features

- ✅ Job submission via FastAPI `/submit-job` endpoint
- 🔄 Asynchronous job processing using a separate worker
- 📨 AWS SQS message queuing
- 📦 Fully containerized with Docker/Podman
- 🤖 GitHub Actions CI/CD pipeline
- 🔐 Secure AWS access via GitHub Secrets

---

## ⚙️ Technologies Used

- **FastAPI** – for building the job submission API  
- **Python 3.11** – runtime environment  
- **Boto3** – AWS SDK for interacting with SQS  
- **AWS SQS** – decoupled message queue  
- **AWS ECR** – container registry  
- **Poetry** – dependency management  
- **Podman / Docker** – containerization  
- **GitHub Actions** – continuous integration and deployment  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/scalable-job-queue.git
cd scalable-job-queue
```

### 2. Set Up Environment Variables

Create a `.env` file inside `backend/` with the following:

```env
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
SQS_QUEUE_URL=https://sqs.<region>.amazonaws.com/<account_id>/<queue_name>
```

### 3. Run Locally (with Docker Compose)

```bash
cd backend
podman-compose up --build
```

This will start:
- `job-queue-api` on port `8000`
- `job-queue-worker` running in background

---

## 🧪 API Usage

### Submit Job

```bash
curl -X POST http://localhost:8000/submit-job \
  -H "Content-Type: application/json" \
  -d '{
    "task_type": "email",
    "payload": {
      "to": "test@example.com",
      "subject": "Hello"
    }
  }'
```

### Expected Response

```json
{
  "message": "Job submitted successfully",
  "job_id": "e.g. 1c7a4e5a-..."
}
```

---

## 🛠️ GitHub Actions CI/CD

This project uses two GitHub Actions workflows:

- **CI Workflow**:
  - Lints and builds backend
  - Builds & pushes Docker images for API and Worker to ECR

- **Deploy Workflow (optional)**:
  - Can be configured to deploy to ECS or another orchestrator

### Required GitHub Secrets

Add the following in your repo settings under **Settings > Secrets and variables > Actions**:

- `AWS_ACCESS_KEY`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `SQS_QUEUE_URL`

---

## 🐳 Building Manually

### Build and Run API

```bash
cd backend
podman build -f Dockerfile -t job-queue-api .
podman run -p 8000:8000 job-queue-api
```

### Build and Run Worker

```bash
cd backend
podman build -f Dockerfile.worker -t job-queue-worker .
podman run job-queue-worker
```

---

## 📦 Deployment (AWS ECR)

1. GitHub Actions pushes `job-queue-api` and `job-queue-worker` images to ECR
2. You can deploy them to:
   - ECS (Fargate or EC2-backed)
   - EKS (Kubernetes)
   - EC2 instances manually

You can verify the images by going to AWS Console → ECR → Your Repository → Tags.

---

## 💰 AWS Costs

- **SQS**: Free for the first 1 million requests per month
- **ECR**: Charged based on GB stored and data transferred
- **IAM User**: No cost, but don't keep long-lived credentials unused

🛑 **Delete unused images to avoid storage charges**

---

## ✅ TODOs

- [ ] Add retry & dead-letter queue logic
- [ ] Add support for multiple job types and dynamic handlers
- [ ] Add ECS deployment using Terraform/CDK
- [ ] Add automated tests
- [ ] Add Prometheus/Grafana monitoring

---

## 🙋‍♀️ Contributions

Feel free to fork the repo, submit issues or pull requests. All contributions are welcome!