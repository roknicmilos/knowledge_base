# RAG and Amazon Bedrock Knowledge Bases

Read [LLM basics](llm.md) first.

## RAG – Retrieval-Augmented Generation

Combines **retrieval** and **generation** to produce accurate, context-relevant answers.

1. **Retrieval** – fetch relevant information from a knowledge base (documents, databases, vector embeddings) based on
   the user's query; usually via semantic search over [embeddings](concepts/training-and-inference.md#embedding) in a
   vector database.
2. **Augmentation** – inject the retrieved information into the prompt as context.
3. **Generation** – the model answers using the augmented prompt, grounded in the retrieved knowledge.

**Benefits:** better factual accuracy (verifiable sources) · knowledge can be updated without retraining ·
domain-specific answers. **Example:** a support chatbot retrieves FAQs/product docs for a question and writes a coherent
reply. **Design concerns:** chunking strategy, embedding model, hybrid (keyword + vector) search, re-ranking,
context-window limits, evaluation, access control on documents, and what the model should do when nothing relevant is
retrieved.

## Amazon Bedrock Knowledge Bases

Bedrock provides foundation models (from several providers, e.g. Anthropic Claude, Amazon Nova, Meta Llama, Mistral). A
*knowledge base* is a managed workflow that augments those models with your data:

1. **Data storage (e.g. S3)** – source of truth for raw data (product manuals, articles, papers, FAQs); not queried
   directly.
2. **Preprocessing and embeddings** – documents are chunked and an embedding model converts each chunk into a vector.
3. **Vector store** – holds embeddings + metadata (document ID, section tags…) and performs semantic search on the query
   embedding. Supported stores include OpenSearch Serverless, Aurora PostgreSQL (pgvector), Pinecone, MongoDB Atlas,
   Redis, Neptune Analytics, S3 Vectors. *(Verify the current list before choosing; Weaviate is not among the native
   options.)*
4. **Context injection** – the retrieved chunks are added to the prompt sent to the foundation model, which generates
   the answer.

Example flow – "What are the key features of product X?":

1. Convert the query to an embedding.
2. Semantic search in the vector store.
3. Retrieve matching sections ("Product X supports A, B and C").
4. Inject them into the prompt.
5. The model writes a detailed answer from that context.

Why a vector database: fast semantic lookup (meaning, not keywords), scales to large datasets, real-time queries.
Related: [fine-tuning vs prompting vs RAG](fine-tuning-prompting-rag.md), [S3](../devops/cloud/aws/s3.md),
[OpenSearch](../devops/elasticsearch-vs-opensearch.md).
