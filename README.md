# AWS Hands-On Learning

Practical AWS engineering, worked from the ground up — building toward a
production-shaped **ML inference platform**. Focus: SDE / ML infrastructure /
inference / AI engineering.

**Language:** Python (boto3) · **IaC:** Terraform · **Containers:** Docker

## 📍 Roadmap
Full plan and rationale in [ROADMAP.md](ROADMAP.md).

| Phase | Focus | Status |
|---|---|---|
| 0 | Account setup & safety | ✅ done |
| 1 | Core primitives — IAM, S3, EC2, VPC, CloudWatch | 🔄 in progress |
| 2 | Serverless & APIs — Lambda, API Gateway, DynamoDB, RDS, SQS/SNS, Terraform | ⬜ |
| 3 | Containers — Docker, ECR, ECS Fargate | ⬜ |
| 4 | ML/AI — SageMaker, Bedrock, GPU inference | ⬜ |
| 🏆 | Capstone — end-to-end ML inference platform | ⬜ |

## 📂 Structure
```
aws_tutorial/
├── ROADMAP.md          # the full learning plan
├── phase-1-core/       # labs & notes per phase (created as we go)
├── phase-2-serverless/
├── phase-3-containers/
└── ...
```

## 🔒 Safety
This repo never contains credentials or Terraform state (see `.gitignore`).
All resources are torn down after each lab to avoid unexpected costs.
