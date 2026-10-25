# Terraform

An **Infrastructure as Code (IaC)** tool by HashiCorp for defining, provisioning and managing cloud and on-premises
resources in a declarative language (HCL). Docs: <https://developer.hashicorp.com/terraform>

> **Verify (licensing):** since 2023 Terraform uses the Business Source License; **OpenTofu** (Linux Foundation,
> MPL-2.0) is the open-source fork with a compatible workflow. HashiCorp is now part of IBM.

## Key features

- **Multi-cloud** – AWS, Azure, GCP, Kubernetes and thousands of providers.
- **Declarative** – describe what you want; Terraform works out how.
- **State management** – tracks real infrastructure to detect and apply changes safely (use a remote backend with
  locking for teams).
- **Dependency graph** – handles ordering automatically (VPC before subnet).
- **Modules** – reusable, write once.
- **Plan & apply** – preview changes before executing.

## Workflow

1. **Write configuration** (`.tf` files, HCL):
   ```hcl
   data "aws_ami" "al2023" {
     most_recent = true
     owners      = ["amazon"]
     filter {
       name   = "name"
       values = ["al2023-ami-*-x86_64"]
     }
   }

   resource "aws_instance" "web_server" {
     ami           = data.aws_ami.al2023.id   # look up the AMI, don't hard-code region-specific IDs
     instance_type = "t3.micro"
   }
   ```
2. `terraform init` – download provider plugins, configure the backend.
3. `terraform plan` – show what will change (safety check).
4. `terraform apply` – create/update infrastructure.
5. `terraform destroy` – (optional) remove the resources.

Other commands: `terraform fmt` (format), `terraform validate` (syntax + internal consistency), `terraform state`,
`terraform import`.

## Terraform vs alternatives

| Tool                 | Type                                                                                        | Key difference                      |
|----------------------|---------------------------------------------------------------------------------------------|-------------------------------------|
| Terraform / OpenTofu | IaC, declarative                                                                            | Multi-cloud, stateful, modular      |
| Ansible              | Configuration management (modules are declarative/idempotent, playbooks run tasks in order) | Procedural flow, agentless          |
| AWS CloudFormation   | AWS-only IaC                                                                                | Tight AWS integration, JSON/YAML    |
| Pulumi               | IaC in general-purpose languages                                                            | Python/Go/TypeScript instead of HCL |

## Use cases

Cloud provisioning (EC2, Azure VMs, GKE) · Kubernetes management · multi-tier apps (networks, VMs, load balancers, DBs
together) · disposable dev/test environments · GitOps and CI/CD (GitHub Actions, Jenkins, GitLab CI).

## Why use it

Consistency (no manual "click-ops" mistakes) · version control for infrastructure · collaboration/review · quick
disaster recovery (rebuild from code).

See [declarative vs imperative](../fundamentals/declarative-vs-imperative.md), [CI/CD](ci-cd.md).
