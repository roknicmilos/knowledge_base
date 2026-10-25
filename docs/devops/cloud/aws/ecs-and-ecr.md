# Amazon ECS and ECR

## ECS – Elastic Container Service

Runs and manages Docker containers on AWS.

- **Cluster** – logical group of compute (EC2 instances or Fargate) where containers run.
- **Task definition** – describes containers (image, CPU/memory, ports, roles).
- **Task** – the smallest deployable unit; a running instance of a task definition. Run standalone or as part of a
  **service**
  (keeps N tasks running, scaling, load balancer integration, high availability).

ECS manages clusters, clusters run tasks, tasks are Docker containers doing the work.

|                      | ECS on EC2 (self-managed)                                      | ECS with Fargate                                                                                    |
|----------------------|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Infrastructure       | You manage the EC2 instances (provisioning, scaling, patching) | Fully managed by AWS (serverless)                                                                   |
| Scaling              | Manual or auto-scaling of EC2                                  | Automatic container scaling                                                                         |
| Cost model           | Pay for EC2 instances (spot/reserved to optimize)              | Pay per vCPU/memory used                                                                            |
| Customization        | Full control (AMIs, OS tuning, instance types)                 | Limited to container resources                                                                      |
| Operational overhead | High                                                           | Low                                                                                                 |
| GPU                  | Yes                                                            | Not supported at the time of writing (*verify – newer options such as ECS Managed Instances exist*) |

**Choose ECS on EC2** for fine-grained infrastructure control, cost optimization (spot, custom scaling), steady
predictable
workloads. **Choose Fargate** for simplicity/no infrastructure management, unpredictable scaling, small or
serverless-first
workloads, when slightly higher cost for lower operations is acceptable.

## ECR – Elastic Container Registry

AWS's private container registry. ECR + ECS is the standard combination:

1. **Seamless integration** – ECS pulls images from ECR natively.
2. **AWS ecosystem** – works with IAM, CloudWatch, CodePipeline.
3. **Simple workflow** – push in CI/CD, update the task definition, ECS deploys.
4. **Security** – IAM-controlled access; the task *execution role* lets ECS pull images without exposing credentials.
5. **Scalability** – handles many images and pulls.

Typical workflow: **Build** the image (locally/CI) → **Push** to ECR → **Deploy** by updating the task definition with
the new
image → **Run**: ECS pulls the image and starts the container.

Not the only option: Docker Hub or GitHub Container Registry work with ECS too, but ECR is preferred on AWS for
integration and
security.
