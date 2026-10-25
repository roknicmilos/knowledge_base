# Fine-tuning vs prompt engineering vs RAG

Three ways to adapt an LLM ([LLM basics](llm.md)).

## Fine-tuning

Further training a pretrained model (e.g. GPT) on a specific dataset for a task or domain, adjusting its weights.

How:

1. Start from a pretrained general-purpose LLM.
2. Provide a curated domain dataset (medical records, legal texts, support logs).
3. Train further (typically supervised; parameter-efficient methods such as LoRA are common; preference tuning like
   RLHF/DPO is
   also used).

**Advantages:** high task-specific accuracy · domain terminology and style · consistent behavior with shorter prompts.
**Disadvantages:** compute-intensive · static (re-tune to change or add tasks) · needs a sufficiently large,
high-quality dataset.

## Prompt engineering

Designing the input prompt to elicit the desired behavior **without** changing the model's parameters.

How:

1. **Task description** – structured instructions ("Summarize this legal document in 100 words").
2. **Zero-shot / few-shot** – rely on generalization, or include examples in the prompt.
3. **Iterate and test** – refine wording, context, examples.

**Advantages:** quick, no retraining, versatile (one model, many tasks), no specialized dataset. **Disadvantages:**
results vary with wording · may lack depth on specialized tasks · complex tasks need much experimentation.

*Prompt design vs prompt engineering* (one vendor's framing – the distinction is not universal): design = writing the
instructions/context for a task; engineering = the broader practice of developing and optimizing prompts, possibly with
domain
knowledge, examples and effective keywords, for systems needing higher accuracy.

## RAG

Retrieval-Augmented Generation retrieves relevant external data at query time and injects it into the prompt. Details:
[RAG and Amazon Bedrock](rag.md).

## Comparison

|                         | Prompt engineering                 | RAG                                             | Fine-tuning                                           |
|-------------------------|------------------------------------|-------------------------------------------------|-------------------------------------------------------|
| Key benefit             | Rapid adaptability and prototyping | Real-time/external data for factual answers     | High specialization, tailored responses               |
| Training required       | No                                 | No                                              | Yes                                                   |
| External data           | No                                 | Needs a corpus                                  | Task-specific dataset                                 |
| Computation             | No overhead                        | Overhead for retrieval                          | Intensive for training, none extra at inference       |
| Quality improvement     | Iterative refinement               | Update/expand the corpus                        | Periodic retraining                                   |
| Potential costs         | Human effort crafting prompts      | Storing/indexing the corpus, retrieval overhead | Dataset, training compute, evaluation                 |
| Technical complexity    | Low                                | Moderate to high (corpus management)            | Moderate (needs ML expertise, dataset bias awareness) |
| Extra inference latency | No                                 | Yes (retrieval)                                 | No                                                    |

Venn view: prompt engineering is easy and good for prototyping but limited to the context window; RAG connects external,
dynamic, real-time knowledge; fine-tuning narrows/steers model behavior and bakes in style, tone and format. Combined
they give
the best outputs.

## When to use what

- **Fine-tuning:** high accuracy for a specific task (legal summarization, medical), specialized terminology not well
  covered by
  general training data, repeated same task without re-instructing.
- **Prompt engineering:** flexibility across tasks/domains, no data or resources to fine-tune, quick experiments,
  one-off tasks.
- **RAG:** answers must be grounded in your own, changing documents.
- **Combine:** e.g. fine-tune on customer-support data for your business, then use prompts to handle FAQs, draft email
  replies
  and summarize chats – and add RAG for up-to-date product facts.
