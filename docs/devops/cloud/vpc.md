# Cloud basics and VPC

## Cloud computing basics (external notes)

- [Basics of cloud computing](https://github.com/iam-veeramalla/gcp-zero-to-hero/blob/main/day-01/01-cloud-computing.md)
- [Basic vocabulary](https://github.com/iam-veeramalla/gcp-zero-to-hero/blob/main/day-01/02-vocabulary.md)

> **TODO:** write the core vocabulary here (region, zone, IaaS/PaaS/SaaS, shared responsibility, elasticity…) instead of
> only
> linking to a third-party course.

## VPC – Virtual Private Cloud

Your own private, isolated network inside the cloud – a virtual mini data center. A VPC lets you define:

- private IP ranges, subnets (public/private), routing rules,
- firewalls / security groups,
- VPN / peering connections,
- which resources are exposed to the internet and which are internal.

(AWS VPCs are regional; GCP VPCs are global with regional subnets.)

### How many VPCs?

1. **One VPC for everything** – almost never recommended: hard to isolate environments/projects, networking turns into
   spaghetti,
   huge security blast radius, hard to delegate access. Seen in tiny startups or legacy setups.
2. **One VPC per environment** (`vpc-prod`, `vpc-staging`, `vpc-dev`) – common. Projects inside are separated by
   subnets,
   namespaces, IAM and services (GKE, ECS, Lambda…). Good balance of cost, simplicity and security; typical for mid-size
   companies.
3. **One VPC per project** (`marketing-app-vpc`, `auth-service-vpc`, `payments-vpc`) – strong isolation, different
   network needs per
   project, easier cost attribution, less risk of one team breaking another's networking. Big enterprises/regulated
   industries.
4. **One VPC per project per environment** (`payments-prod`, `payments-staging`, `payments-dev`) – most isolated, most
   overhead.
   For high compliance, strong isolation, many independent teams, a central networking team.

**Recommended default:** VPC-per-environment, and give a project its own VPC only when it has special security or
networking
needs.

Note that the stronger boundary is usually *separate cloud accounts/projects per environment* (AWS accounts, GCP
projects) –
use that in addition to VPC separation.
