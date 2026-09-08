# Lab 2 — EC2 (Elastic Compute Cloud)

**Goal:** launch a real Linux VM, connect to it **without SSH keys** (via SSM Session
Manager), run a command on it, then terminate everything — all from the CLI.

## Mental model
- **EC2 = renting virtual servers ("instances") by the second.** A real Linux/Windows machine in an AWS data center that you fully control.
- It's the **raw compute primitive**. "Serverless" (Lambda, Fargate) runs on EC2 under the hood — knowing the VM makes you a better engineer.
- For ML: **GPU inference** (g5, p4, inf2 instances) runs on EC2. This is core ML-infra territory.

## The 5 building blocks of an instance
Every EC2 instance is defined by choices in these dimensions:
| Block | Question it answers | Our choice |
|---|---|---|
| **AMI** | which OS image? | Amazon Linux 2023 |
| **Instance type** | how big (CPU/RAM)? | `t3.micro` (Free Tier) |
| **Network** (VPC/subnet) | where does it live? | default VPC |
| **Security group** | who can reach it? | no inbound needed (SSM is outbound-only!) |
| **IAM role** | what can *it* do? | SSM-managed role, so we can connect |

## Why SSM instead of SSH?
- **No key pairs to manage/lose**, **no port 22 open to the internet** (a top attack vector).
- The instance reaches *out* to AWS over HTTPS; you connect through AWS. Nothing inbound.
- This is the modern, secure default — and it teaches IAM **roles** (how a service gets permissions).

## ⚠️ COST DISCIPLINE
- `t3.micro` is Free Tier (750 hrs/month), but **a running instance bills by the hour.**
- **ALWAYS terminate** at the end of the lab. We tear down the instance + role + security group.
- `stop` = paused (no compute charge, small storage charge). `terminate` = gone forever.
