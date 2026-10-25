# OpenSearch vs Elasticsearch

Both are Lucene-based search and analytics engines. OpenSearch was forked from Elasticsearch 7.10.2 in 2021 after
Elastic moved
away from Apache 2.0.

## At a glance

|                          | Elasticsearch                                                                           | OpenSearch                                                                          |
|--------------------------|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Created by               | Elastic NV (2010)                                                                       | Fork of ES 7.10.2 (2021), started by AWS                                            |
| License                  | Apache 2.0 until 2021; then SSPL/Elastic License; **AGPLv3 added as an option in 2024** | Apache 2.0                                                                          |
| Governance               | Elastic NV                                                                              | OpenSearch Software Foundation (Linux Foundation, 2024); AWS is a major contributor |
| Search & analytics       | Mature, extensive                                                                       | Similar, behind in some areas                                                       |
| Security                 | Basic security (TLS, RBAC) free since 6.8/7.1; advanced features paid                   | Built-in, free (OpenSearch Security plugin)                                         |
| Machine learning         | Advanced, mostly paid tiers                                                             | Basic, free, improving                                                              |
| Dashboards               | Kibana                                                                                  | OpenSearch Dashboards (open source)                                                 |
| Ingestion                | Logstash, Beats, Elastic Agent                                                          | Data Prepper, Fluentd/Fluent Bit, Logstash                                          |
| Managed offering         | Elastic Cloud (runs on AWS, GCP, Azure)                                                 | Amazon OpenSearch Service, self-hosted                                              |
| Vector / semantic search | Yes                                                                                     | Yes                                                                                 |

> **Verify:** licensing and feature gaps keep changing – check the current license pages before deciding.

## Choosing

**Elasticsearch** if you need its advanced (partly proprietary) features, already use the Elastic stack, or accept
SSPL/Elastic
License/AGPL terms. **OpenSearch** if you prioritize Apache-2.0 open source, want to avoid vendor lock-in, use AWS or
want free security/alerting,
or are migrating from Elasticsearch 7.x.
