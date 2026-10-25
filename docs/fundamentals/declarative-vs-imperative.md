# Declarative vs imperative

|              | Declarative                                                                         | Imperative                          |
|--------------|-------------------------------------------------------------------------------------|-------------------------------------|
| Focus        | **What** – the desired end state                                                    | **How** – step-by-step instructions |
| Approach     | Abstract, high-level                                                                | Explicit, detailed                  |
| Control flow | No explicit loops/branches                                                          | Loops, conditionals, sequences      |
| Examples     | SQL, Terraform, HTML/CSS (markup), Kubernetes manifests, Ansible playbook *modules* | Python, Bash, JavaScript, Java      |
| Flexibility  | Less control over how it's done                                                     | Full control                        |
| Readability  | Concise                                                                             | More verbose                        |
| Typical use  | Config, infrastructure, queries                                                     | Scripting, application logic        |

Note: Ansible is a mix – individual modules are declarative/idempotent, but a playbook runs tasks in order (the
Terraform comparison in [terraform.md](../devops/terraform.md) calls it procedural).
