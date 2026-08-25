# Lab 1 — S3 (Simple Storage Service)

**Goal:** create a bucket, put/list/get/delete objects, generate a presigned URL,
turn on versioning — using **both** the AWS CLI and Python (boto3) — then tear it all down.

## Mental model
- **S3 = object storage.** Not a filesystem, not a disk. You store *objects* (files + metadata) addressed by a **key** (the "path-like" name).
- A **bucket** is a top-level container. **Bucket names are globally unique across all of AWS** — if someone worldwide took the name, you can't.
- Objects are private by default. Access is granted explicitly (IAM, bucket policy, or presigned URL) — never make a bucket public unless you truly mean to.
- S3 is where **model artifacts, datasets, logs, and static assets** live in almost every AWS system.

## Key CLI commands
| Command | What it does |
|---|---|
| `aws s3 mb s3://NAME` | make bucket |
| `aws s3 cp FILE s3://NAME/KEY` | upload |
| `aws s3 ls s3://NAME` | list objects |
| `aws s3 cp s3://NAME/KEY FILE` | download |
| `aws s3 rm s3://NAME/KEY` | delete object |
| `aws s3 rb s3://NAME` | remove (empty) bucket |

`aws s3` = high-level file-like commands. `aws s3api` = low-level, full API control.

## Teardown (always do this)
```
aws s3 rm s3://NAME --recursive   # empty it
aws s3 rb s3://NAME               # delete the bucket
```
