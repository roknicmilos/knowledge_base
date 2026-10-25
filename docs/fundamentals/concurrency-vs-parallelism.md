# Concurrency vs parallelism

- **Concurrency** is about *structure* – dealing with multiple tasks in overlapping time periods (not necessarily at the
  same instant).
- **Parallelism** is about *execution* – literally running multiple tasks at the same time (needs multiple cores).
- Concurrency can exist without parallelism (single-core CPU, time-slicing). Parallelism usually involves concurrency
  (tasks must be coordinated). Modern systems use both.

|          | Concurrency                                                 | Parallelism                                   |
|----------|-------------------------------------------------------------|-----------------------------------------------|
| Idea     | Make progress on many tasks by interleaving                 | Do many tasks simultaneously                  |
| Example  | One core switching between threads                          | Multi-core CPU, one task per core             |
| Best for | I/O-bound work (network, disk, user input) – responsiveness | CPU-bound work (computation, data processing) |

Python specifics (threads vs asyncio vs processes, the GIL): [Python concurrency](../languages/python/concurrency.md).
