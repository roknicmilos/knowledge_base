# Knowledge Base

Personal notes on software engineering, migrated from Google Docs (export reviewed 2026-10-25).
Corrections from the review are already applied; time-sensitive facts are marked `> **Verify:**`.

## Structure

| Folder                                 | Contents                                                                             |
|----------------------------------------|--------------------------------------------------------------------------------------|
| [web/](web/)                           | HTTP, HTTPS/TLS, DNS, CORS, browser storage, AJAX                                    |
| [security/](security/)                 | Password hashing, CSRF                                                               |
| [fundamentals/](fundamentals/)         | OOP, SOLID, typing, exceptions, DI, concurrency, mocking, paradigms, FSM             |
| [computer-science/](computer-science/) | Data structures, algorithms, Big O                                                   |
| [design/](design/)                     | UML/ERD modeling, MVC/MVVM                                                           |
| [architecture/](architecture/)         | Scaling, load balancer, API gateway, monolith vs microservices, REST, caching/CDN, … |
| [databases/](databases/)               | SQL vs NoSQL, indexes, views, transactions, FKs, query performance, N+1              |
| [frontend/](frontend/)                 | React vs Angular, Next.js API layer and auth                                         |
| [languages/](languages/)               | Python (incl. frameworks), Java, C#, PHP                                             |
| [devops/](devops/)                     | CI/CD, cloud (VPC, AWS, GCP), Terraform, Kafka, search                               |
| [ai/](ai/)                             | LLMs, fine-tuning vs prompting vs RAG, Bedrock, iPaaS                                |
| [tools/](tools/)                       | Git commit messages                                                                  |

## Open TODOs (carried over from the original docs)

- Lambda: how to test/debug/monitor, error handling and retries, roles/IAM
  ([devops/cloud/aws/lambda.md](devops/cloud/aws/lambda.md))
- GCP basics: project setup & billing, IAM, Compute Engine, GCS ([devops/cloud/gcp.md](devops/cloud/gcp.md))
- Django security beyond CSRF ([languages/python/frameworks/django.md](languages/python/frameworks/django.md))
- Python: design patterns, data types ([languages/python/README.md](languages/python/README.md))
- iPaaS: deeper notes ([ai/ipaas.md](ai/ipaas.md))
- Not exported from Google Drive: "Technical interview questions (and answers)" and "Basics of LLMs" docs

Code samples referenced originally live in <https://github.com/roknicmilos/python-stuff>.
