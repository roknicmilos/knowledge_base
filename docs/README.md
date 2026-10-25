# Knowledge Base

Personal notes on software engineering, migrated from Google Docs (export reviewed 2026-10-25). Corrections from the
review are already applied; time-sensitive facts are marked `> **Verify:**`.

## Structure

| Folder                                          | Contents                                                                                    |
|-------------------------------------------------|---------------------------------------------------------------------------------------------|
| [web/](web/README.md)                           | HTTP, HTTPS/TLS, DNS, CORS, browser storage, AJAX                                           |
| [security/](security/README.md)                 | Password hashing, CSRF                                                                      |
| [fundamentals/](fundamentals/README.md)         | OOP, SOLID, typing, exceptions, DI, concurrency, mocking, paradigms, FSM                    |
| [computer-science/](computer-science/README.md) | Data structures, algorithms, Big O                                                          |
| [design/](design/README.md)                     | UML/ERD modeling, MVC/MVVM                                                                  |
| [architecture/](architecture/README.md)         | Scaling, load balancer, API gateway, monolith vs microservices, REST, caching/CDN, iPaaS, … |
| [databases/](databases/README.md)               | SQL vs NoSQL, indexes, views, transactions, FKs, query performance, N+1                     |
| [frontend/](frontend/README.md)                 | React vs Angular, Next.js API layer and auth                                                |
| [languages/](languages/README.md)               | Python (incl. frameworks), Java, C#, PHP                                                    |
| [devops/](devops/README.md)                     | CI/CD, cloud (VPC, AWS, GCP), Terraform, Kafka, search                                      |
| [ai/](ai/README.md)                             | LLMs, limitations, RAG, prompting, agents, Claude Code and the Claude API                   |
| [tools/](tools/README.md)                       | Git commit messages                                                                         |

## Open TODOs (carried over from the original docs)

- Lambda: how to test/debug/monitor, error handling and retries, roles/IAM
  ([devops/cloud/aws/lambda.md](devops/cloud/aws/lambda.md))
- GCP basics: project setup & billing, IAM, Compute Engine, GCS ([devops/cloud/gcp.md](devops/cloud/gcp.md))
- Django security beyond CSRF ([languages/python/frameworks/django.md](languages/python/frameworks/django.md))
- Python: design patterns, data types ([languages/python/README.md](languages/python/README.md))
- iPaaS: deeper notes ([architecture/ipaas.md](architecture/ipaas.md))
- Not exported from Google Drive: "Technical interview questions (and answers)" and "Basics of LLMs" docs

Runnable code samples live in [`../examples/`](../examples/README.md).
