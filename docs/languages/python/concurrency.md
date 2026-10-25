# Concurrency, parallelism and the GIL in Python

Concept background: [concurrency vs parallelism](../../fundamentals/concurrency-vs-parallelism.md). Based on [Speed Up
Your Python Program With Concurrency (Real Python)](https://realpython.com/python-concurrency/) – summarized in own
words.

In Python, the "things happening simultaneously" have different names (thread, task, process) but all are a sequence of
instructions running in order. Only **multiprocessing** runs them literally at the same time; threading and asyncio take
turns on one CPU – still called concurrency.

| Concurrency type                       | Who decides when to switch                       | Processors                        |
|----------------------------------------|--------------------------------------------------|-----------------------------------|
| Pre-emptive multitasking (`threading`) | The OS, outside Python's control                 | 1 (at a time, because of the GIL) |
| Cooperative multitasking (`asyncio`)   | The tasks themselves hand control back (`await`) | 1                                 |
| Multiprocessing (`multiprocessing`)    | All processes run at the same time               | Many                              |

## I/O-bound vs CPU-bound

- **I/O-bound:** slow because the program waits for external resources (network, disk, DB). Concurrency helps by using
  the waiting time.
- **CPU-bound:** slow because it computes a lot; no waiting. Threads/asyncio don't help (and add overhead); you need
  more CPUs → multiprocessing.

## threading (I/O-bound)

- Threads share memory; the OS can interrupt them at any moment, so shared data must be protected (thread-safe) – race
  conditions cause random, intermittent bugs.
- **How many threads?** No constant: experiment. `ThreadPoolExecutor` defaults to `min(32, os.cpu_count() + 4)` workers
  (3.8+) and has no hard maximum. For I/O-bound work many more threads than cores can help; thousands usually hurt
  (memory, context switching).
- Cons: more code, subtle bugs.

## asyncio (I/O-bound)

- A single **event loop** decides which task runs; tasks run until they `await`, so they are never interrupted
  mid-operation → easier resource sharing, no thread-safety worries.
- Scales much better than threads (tasks are cheap).
- Cons: needs async-aware libraries (shrinking problem); a task that never yields blocks everything.
- Rule of thumb: **"use asyncio when you can, threading when you must."**

## multiprocessing (CPU-bound)

- Starts a separate interpreter (own memory, own GIL) per process and farms work out to them; fully uses multi-core
  CPUs.
- Cons: extra setup; data must be passed between processes (pickling, or globals via the pool `initializer`); more
  start-up cost (slower than threads/asyncio for I/O-bound work – not what it is for); splitting a problem so processes
  work independently can be hard.
- The default start method changes across versions/platforms (e.g. `forkserver` becomes the Linux default in 3.14).

## When to use concurrency

Concurrency adds complexity and hard-to-find bugs. Wait for a known performance problem ("premature optimization is the
root of all evil" – Knuth), then work out whether it's CPU- or I/O-bound and pick: CPU-bound → multiprocessing;
I/O-bound → asyncio if libraries allow, else threading.

## Coroutines

A coroutine generalizes a subroutine: it can be **suspended and resumed** at defined points, keeping its local state, so
other code can run meanwhile. In Python they're defined with `async def` and driven by `await` / the `asyncio` event
loop; many coroutines run on one thread, using far fewer resources than threads. Ideal for network servers/clients and
anything waiting on external events.

## GIL – Global Interpreter Lock

- A mutex in **CPython** that lets only one thread execute Python bytecode at a time, even on multi-core CPUs; other
  threads wait for the lock.
- Exists to keep CPython's memory management simple and safe – reference counting isn't thread-safe by itself.
- **I/O-bound code is barely affected** – threads release the GIL while waiting. **CPU-bound** threaded code can't run
  in parallel.
- The GIL protects the interpreter's internals, **not your code** – race conditions (e.g. `counter += 1`) still happen;
  use locks/queues.

How people deal with it:

- `multiprocessing` / `concurrent.futures.ProcessPoolExecutor` – each process has its own GIL.
- C extensions/NumPy release the GIL during native computation.
- `asyncio` for I/O concurrency.
- Other runtimes: IronPython has no GIL. (**PyPy has a GIL; Jython is Python 2 only.**)
- Cython `with nogil:` blocks.

> **Verify:** the picture is changing. Free-threaded (no-GIL) builds (PEP 703) were experimental in 3.13 and officially
> supported in 3.14 (PEP 779), but are not the default; per-interpreter GILs/sub-interpreters exist since 3.12. Check
> current docs before choosing a strategy.
