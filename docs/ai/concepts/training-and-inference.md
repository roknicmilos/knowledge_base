# Training, fine-tuning, inference and embeddings

The lifecycle of a model and the building block behind semantic search.

## Pre-training

The initial, large-scale pass that turns a randomly initialized network into a base model by predicting the next token
over a massive, broad corpus. It is where general language ability, world knowledge and reasoning patterns come from, and
what sets the [knowledge cutoff](../limitations.md#knowledge-cutoff) (the corpus is a fixed snapshot). You don't do it
yourself; it is the extremely expensive, provider-run step.

## Fine-tuning

Further training a pre-trained model on your own, much smaller set of examples to specialize behavior or style. It bakes
patterns into the weights, unlike prompting/RAG which only add context at runtime, and needs far less data and compute
than pre-training because the model already knows language and the world.

Use it when prompting can't reliably get the behavior and you have enough quality examples (e.g. a consistent output
format or house style across thousands of calls). Comparison: [Fine-tuning vs prompt engineering vs
RAG](../fine-tuning-prompting-rag.md). Rule of thumb: RAG for changing facts, fine-tuning for consistent behavior and
format; often combined.

## Inference

*Running* the model to produce output, as opposed to training it. Every response is an inference pass; it is what you pay
for per token in production, and what latency and pricing discussions refer to.

## Embedding

A numeric vector capturing the *meaning* of a text, so similar meanings land near each other in vector space. Generate
with an embedding model, store in a vector index, query by nearest neighbor (e.g. embed a question and pull the closest
support articles). It powers semantic search and [RAG](../rag.md).

Not every retrieval problem needs embeddings: Claude Code finds code with ripgrep (keyword search), glob, direct reads
and LSP, not a vector store.
