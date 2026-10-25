# AWS IAM

Identity and Access Management: controls **who** (identity) can access **which** AWS resources and under **what
conditions**.
IAM is a **global** service.

## Components

| Component   | Description                                                                                    |
|-------------|------------------------------------------------------------------------------------------------|
| Users       | Individual identities for people (or, legacy, applications); own credentials                   |
| Groups      | Collections of users sharing permissions (e.g. "Admins", "Developers")                         |
| Roles       | Temporary credentials for AWS resources or external entities (e.g. an EC2 instance reading S3) |
| Policies    | JSON documents defining allowed/denied actions on resources                                    |
| Access keys | Programmatic (CLI/SDK) access                                                                  |
| MFA         | Multi-factor authentication for extra security                                                 |

- **Fine-grained access control:** permissions via policies attached to users, groups or roles.
- **Policy types:** *managed* (AWS-managed or customer-managed, reusable) and *inline* (embedded in one identity). Also
  resource-based policies (e.g. S3 bucket policies), permission boundaries and Service Control Policies (Organizations).
- **Federated access:** use existing identities (Active Directory, Google, SAML/OIDC) via IAM Identity Center or
  identity providers.

## Common use cases

1. **User management** – create users/credentials, group them.
2. **Resource access control** – e.g. restrict an S3 bucket to certain users/roles.
3. **Temporary credentials** – roles for apps on EC2/Lambda, or cross-account access.
4. **Compliance and security** – enforce least privilege; use IAM Access Analyzer to find overly permissive policies.

## Policy example

Read objects from an S3 bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-bucket/*"
    }
  ]
}
```

(Listing the bucket would additionally need `s3:ListBucket` on `arn:aws:s3:::example-bucket`.)

## Best practices

1. **Least privilege** – grant only what is needed.
2. **MFA** for everyone, especially the root account; don't use root for daily work.
3. **Roles instead of long-lived access keys** for applications (EC2, Lambda, ECS tasks); use **IAM Identity Center (
   SSO)** for
   humans.
4. **Rotate credentials** that must exist.
5. **Audit and monitor** with CloudTrail.

Tools: AWS Console, AWS CLI, SDKs.

## Limitations

- Policies are global but can be restricted by region with conditions (`aws:RequestedRegion`).
- Complexity grows with many users/roles/policies – needs organization and naming conventions.
