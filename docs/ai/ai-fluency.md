# AI fluency (the 4D framework) and cognitive bias

The human-skills side of working with AI.

## The 4Ds

Anthropic's framework for working effectively and responsibly with AI, built on four competencies. It is a human-skills
framework, not a product feature.

| Competency      | Meaning                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| **Delegation**  | Deciding what to hand to AI and what to keep, based on what the AI is actually good at                                  |
| **Description** | Communicating clearly: prompting, context, constraints ([prompt engineering](concepts/prompt-engineering.md))           |
| **Discernment** | Critically evaluating output: catching errors, [hallucinations](limitations.md#hallucination) and bias; trust vs verify |
| **Diligence**   | Taking responsibility for outcomes: quality, ethical and legal considerations                                           |

They work together: efficient, effective, safe and ethical use, not optimizing one at the expense of the others.

Use it as a checklist when handing real work to an [agent](concepts/agents-and-workflows.md#agent) (like delegating to a
new hire): did you delegate the right slice, describe it well, review what came back, and take ownership of what you
ship?

## Cognitive bias

A systematic, predictable error in human judgment. The one that matters most with AI is **automation bias**:
over-trusting an automated system's output and not verifying it just because it came from the system ("trusting the GPS
into a lake").

- It is the human counterpart to a model's [hallucination](limitations.md#hallucination) and
  [sycophancy](limitations.md#sycophancy): the model can be confidently wrong, and automation bias stops a person from
  catching it. It is the failure mode Discernment exists to counter.
- It runs both ways: blanket distrust of any AI output ("algorithm aversion") throws away real value. The fix in both
  directions is to verify against evidence, not against a prior assumption about AI.
