# Prompt evaluation

Systematically testing a prompt against representative inputs and scoring the outputs, instead of judging quality from a
few manual tries. It is a test suite for a prompt: you wouldn't ship code because it worked once.

Each test case is run through the model, the output is scored, and scores roll up into a metric (accuracy, pass rate,
average rubric score) you can compare across prompt versions.

## Grader types

From cheapest/strictest to most flexible:

| Grader                     | How it scores                                             | Pros                                    | Cons                                            |
|----------------------------|-----------------------------------------------------------|-----------------------------------------|-------------------------------------------------|
| Code-based                 | Exact/fuzzy match, regex, JSON-schema check, unit test    | Fast, cheap, perfectly consistent       | Only when correctness is mechanically checkable |
| Model-based (LLM-as-judge) | Another LLM call scores against a rubric/reference answer | Handles subjective, open-ended criteria | Costs tokens; inherits the judge's blind spots  |
| Human                      | A person applies a rubric or picks A vs B                 | Highest-quality signal                  | Slow, expensive, doesn't scale                  |

Anthropic's Console has a built-in Evaluation tool; teams also write custom scripts that loop over a dataset and call
the API for CI-style regression testing.

## Gotchas

- A prompt that looks better on a handful of tries can regress on cases outside that sample. Evals catch this because
  they check a fixed set every time; they don't replace manual review entirely.
- LLM-as-judge is a cheaper substitute for human grading, not an infallible one: periodically spot-check its
  calibration with human graders.

Related: [Prompt engineering](prompt-engineering.md), [Sampling and determinism](sampling-and-determinism.md).
