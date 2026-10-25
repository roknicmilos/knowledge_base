# LLMs – Large Language Models

> Source: the "Technical interview questions" section of the old main doc. The original Google Docs "Technical interview
> questions (and answers)" and "Basics of LLMs" were not part of the export – compare if they contain more.

An LLM is a machine-learning model trained on massive amounts of text to understand, generate and process natural
language:
text generation, translation, summarization, question answering and more.

Relationship: LLMs and **Generative AI** overlap and both sit inside **Deep Learning** (which is part of ML). Generative
AI is
AI that produces new content – text, images, audio, synthetic data.

| Aspect        | LLM                                                                   | Generative AI                         |
|---------------|-----------------------------------------------------------------------|---------------------------------------|
| Scope         | Natural-language processing/text                                      | Broad: text, images, video, audio, 3D |
| Type          | A specific model type within Generative AI                            | A general category of techniques      |
| Examples      | GPT, Claude, Gemini, Llama (BERT is an encoder model, not generative) | GPT, DALL·E, Stable Diffusion, …      |
| Input/output  | Textual                                                               | Multimodal                            |
| Training data | Text (books, articles, web)                                           | Multimodal datasets                   |
| Applications  | Chatbots, summarization, code                                         | Art/video/audio generation, etc.      |

## Characteristics

- **Large-scale architecture** – billions (or more) of parameters (the weights that determine behavior).
- **Pretraining** on diverse text (books, articles, websites) to learn language patterns, grammar and context.
- **Generative** – produce human-like text by predicting the next **token** given the prompt.
- **Adaptable** – via fine-tuning or prompt engineering to tasks/domains.

> **Verify:** model names change quickly (the old notes cited GPT-4, PaLM, LLaMA; PaLM has been retired in favour of
> Gemini).

## How LLMs work

1. **Transformers** – most LLMs use the transformer architecture ("Attention Is All You Need", 2017); *self-attention*
   lets the
   model focus on relevant parts of the input.
2. **Training** – pretrained with self-supervised learning on large datasets, then often instruction-tuned and aligned
   (e.g. with human feedback), and optionally fine-tuned for tasks.
3. **Tokenization** – text is split into tokens (words, subwords, characters).
4. **Prediction** – repeatedly predict the most probable next token to generate a response.

## Use cases

Text and code generation (writing, explaining, debugging) · chatbots and assistants · translation · summarization ·
sentiment
analysis.

## Challenges and limitations

- **Resource-intensive** training and inference.
- **Bias** inherited from training data.
- **No human-like understanding** – pattern-based generation rather than reasoning in the human sense.
- **Hallucination** – confident but incorrect or nonsensical output.

## LLM development vs traditional ML development

- With an LLM you can often start with **prompt design** – writing clear, concise, informative prompts – with no model
  training and
  far fewer labeled examples. You still need evaluation data and engineering discipline to get reliable results.
- Traditional ML typically needs expertise, labeled training data, compute time and hardware to train a model.

Next: [fine-tuning vs prompt engineering vs RAG](fine-tuning-prompting-rag.md).
