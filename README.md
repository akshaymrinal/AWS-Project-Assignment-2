# Autosave EC2 Instance State Before Shutdown

## Project Overview

This project demonstrates an automated AWS serverless solution that captures and stores EC2 instance state information in an Amazon S3 bucket whenever an EC2 instance is terminated.

## Objective

Automatically save EC2 instance state information before shutdown or termination using:
- Amazon EventBridge
- AWS Lambda
- Amazon S3
- Amazon EC2
- IAM

## Architecture

```text
EC2 Instance
     │
     ▼
EventBridge Rule
     │
     ▼
AWS Lambda
     │
     ▼
Amazon S3 Bucket
```

## AWS Services Used

- Amazon EC2
- AWS Lambda
- Amazon EventBridge
- Amazon S3
- AWS IAM
- Amazon CloudWatch

## Repository Structure

```text
autosave-ec2-state/
├── lambda/
├── iam/
├── eventbridge/
├── screenshots/
└── README.md
```

## Expected Results

- EventBridge detects EC2 termination.
- Lambda executes automatically.
- Instance metadata is collected.
- Backup JSON file is stored in S3.

