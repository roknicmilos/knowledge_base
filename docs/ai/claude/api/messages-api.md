# Messages API basics: chat and streaming

Minimal Python examples with the `anthropic` SDK. The API is stateless: you keep the conversation list and resend it on
every call.

Setup: a virtual environment with `anthropic` and `python-dotenv`; the API key goes in a `.env` file
(`ANTHROPIC_API_KEY`). Runnable notebooks:
[`practical/claude_api`](https://github.com/roknicmilos/learn_claude_code/tree/main/practical/claude_api).

> **Verify:** the notebooks use `model = "claude-sonnet-5"`. Check the current model IDs before copying.

## Synchronous chat

```python
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-5"


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        # system="System prompt message",
        # temperature=0.5,
    )
    return message.content[0].text


messages = []
add_user_message(messages, "Define quantum computing in one sentence")
answer = chat(messages)

add_assistant_message(messages, answer)  # keep the history yourself
add_user_message(messages, "Write another sentence")
answer = chat(messages)
```

- `system` sets the standing instructions (see [prompt engineering](../../concepts/prompt-engineering.md)).
- `temperature` is a request parameter ([sampling](../../concepts/sampling-and-determinism.md)).
- `max_tokens` is required and caps the output.

## Streaming

Prefer the `messages.stream` helper over `create(..., stream=True)` (which yields raw events you have to unpack):

```python
with client.messages.stream(model=model, max_tokens=1000, messages=messages) as stream:
    for text in stream.text_stream:
        print(text, end="")

final_message = stream.get_final_message()
```
