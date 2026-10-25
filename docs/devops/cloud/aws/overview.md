# AWS overview

Amazon Web Services – a comprehensive cloud platform offering compute, storage, databases, ML, analytics, networking and
more
over the internet, without owning physical hardware.

## Key features

- **On-demand, pay-as-you-go** – no upfront cost (unless you choose reserved capacity/savings plans).
- **Global infrastructure** – regions and availability zones for high availability, fault tolerance and low latency.
- **Scalability** – scale resources up or down with demand.
- **Security** – encryption, IAM, compliance certifications.
- **Breadth** – well over 200 services.

## Core services

| Area                  | Services                                                                                                         |
|-----------------------|------------------------------------------------------------------------------------------------------------------|
| Compute               | EC2 (virtual servers), [Lambda](lambda.md) (serverless), Elastic Beanstalk (PaaS), [ECS/Fargate](ecs-and-ecr.md) |
| Storage               | [S3](s3.md) (object), EBS (block for EC2), S3 Glacier storage classes (archive)                                  |
| Databases             | RDS (managed relational), DynamoDB (NoSQL), Redshift (data warehouse)                                            |
| Networking            | VPC, Route 53 (DNS), CloudFront (CDN)                                                                            |
| ML & AI               | SageMaker, Rekognition (image/video), Polly (text-to-speech), [Bedrock](../../../ai/rag.md)                      |
| Management            | CloudWatch (monitoring), CloudFormation (IaC), [IAM](iam.md)                                                     |
| Developer tools       | CodePipeline (CI/CD), CodeBuild, CodeCommit                                                                      |
| Security & compliance | Shield (DDoS), KMS (keys), Artifact (compliance reports)                                                         |

> **Verify:** AWS CodeCommit stopped accepting new customers in 2024 and its status has changed since – prefer
> GitHub/GitLab
> unless you have a reason.

## Benefits

Cost-effective (spot, reserved instances), flexible (many OSes/languages/frameworks), reliable (multi-region/AZ),
scalable,
globally available, constantly innovating.

Related: [VPC](../vpc.md), [Terraform](../../terraform.md).
