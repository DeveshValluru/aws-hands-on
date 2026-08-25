# AWS Hands-On Roadmap — SDE / ML Infra / Inference / AI Engineer

Goal: turn Cloud Practitioner theory into real, demonstrable skills, ending with a
**showcase ML inference platform** you can put on your resume and talk about in interviews.

Language: **Python** (boto3 SDK). IaC: **Terraform**. Containers: **Docker**.

---

## How this works

Each phase has: concepts to know → a small hands-on lab → a checkpoint.
We build in this folder. Everything is real AWS (mostly Free Tier). We tear down
resources after each lab so you never get surprise bills.

**Progress is tracked in the task list** — ask me "what's next?" anytime.

---

## Phase 0 — Setup & Safety  *(do this first, ~30 min)*
The #1 way new grads get burned: leaving expensive resources running.
- [ ] Create AWS account
- [ ] Stop using the **root** user — create an **IAM admin user** with MFA
- [ ] Set a **Budget alert** ($5–10) so AWS emails you if spend climbs
- [ ] Install **AWS CLI**, run `aws configure`
- [ ] Install **boto3** (`pip install boto3`)
- [ ] Understand **Free Tier** limits and what costs money

## Phase 1 — Core Primitives  *(the essentials everyone must know)*
- **Regions & Availability Zones** — the map underneath everything (latency, cost, HA)
- **IAM** — users, roles, policies (the thing most people get wrong)
- **S3** — object storage, buckets, presigned URLs, versioning
- **EC2** — launch a VM, connect via **SSM Session Manager** (no SSH keys), security groups
- **VPC basics** — subnets (public vs private), security groups, internet vs NAT gateway
- **CloudWatch** — logs & metrics
- **Cost tagging + Cost Explorer** — tag resources, see what each project costs
- *(awareness only: CloudTrail = audit log, KMS = encryption keys)*
- 🔬 **Lab / Project 1:** Host + serve files from S3, manage it entirely from the CLI and boto3

## Phase 2 — Serverless & APIs  *(bread and butter for SDE + inference endpoints)*
- **Lambda** (Python) — event-driven compute
- **API Gateway** — turn a Lambda into an HTTP API
- **DynamoDB** — serverless NoSQL
- **RDS** — managed relational DB (Postgres); when to pick SQL vs NoSQL
- **Secrets management** — Secrets Manager / SSM Parameter Store (never hardcode creds)
- **Messaging & events** — **SQS** (queues), **SNS** (pub/sub), **EventBridge**; the async/batch-inference pattern
- **IaC intro** — deploy the above with **Terraform** instead of clicking
- 🔬 **Project 2:** Serverless REST API (Lambda + API Gateway + DynamoDB), fully in Terraform

## Phase 3 — Containers  *(the heart of ML infra / model serving)*
- **Docker → ECR** — build an image, push to AWS registry
- **ECS Fargate** — run containers without managing servers
- **Load balancing & autoscaling** basics — **ALB vs NLB**, scaling on demand
- **Route 53 + ACM** — custom domain + free HTTPS certificate
- *(awareness only: **EKS**/Kubernetes, **App Runner**/Elastic Beanstalk as lighter deploy options)*
- 🔬 **Project 3:** Containerize a Python inference service, deploy on ECS Fargate

## Phase 4 — ML / AI on AWS  *(your differentiator)*
- **SageMaker** — managed model endpoints, batch transform
- **Bedrock** — calling foundation models (LLMs) via API
- **GPU instances** & cost control for inference
- **Model artifact management** with S3, versioning
- Inference patterns: real-time endpoint vs serverless vs batch

## 🏆 Capstone — ML Inference Platform (the showcase)
An end-to-end, production-shaped system that ties everything together:
- Model artifact stored in **S3**
- Inference served via **containerized API on ECS Fargate** (or Lambda for lighter models)
- Public **API Gateway / ALB** endpoint
- Request logging in **DynamoDB**, metrics/alarms in **CloudWatch**
- Entire stack defined in **Terraform** (one command to deploy/destroy)
- **CI/CD** with GitHub Actions
- README with architecture diagram — recruiter- and interviewer-ready

---

## Cost discipline (read this once, live by it)
- **Always `terraform destroy` / delete resources** when a lab is done.
- **Never leave running:** EC2 instances, NAT Gateways, SageMaker endpoints, load balancers, RDS. These bill by the hour even when idle.
- Set the **budget alert** in Phase 0 and check the Billing dashboard weekly.
- Prefer **Free Tier** resource sizes (t2.micro/t3.micro, Lambda, DynamoDB on-demand).
