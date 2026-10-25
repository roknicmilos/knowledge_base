# Python data structures

| Type                                           | Ordered                                          | Mutable                    | Duplicates | Use case                                     |
|------------------------------------------------|--------------------------------------------------|----------------------------|------------|----------------------------------------------|
| `list`                                         | Yes                                              | Yes                        | Yes        | General-purpose collection                   |
| `tuple`                                        | Yes                                              | No                         | Yes        | Immutable record/collection                  |
| `set`                                          | No                                               | Yes                        | No         | Unique items, set operations                 |
| `frozenset`                                    | No                                               | No                         | No         | Immutable sets (dict keys)                   |
| `dict`                                         | **Yes – insertion order (guaranteed since 3.7)** | Yes                        | No (keys)  | Key-value storage                            |
| `str`                                          | Yes                                              | No                         | Yes        | Text                                         |
| `bytes` / `bytearray`                          | Yes                                              | No / Yes                   | Yes        | Binary data                                  |
| `array.array`                                  | Yes                                              | Yes                        | Yes        | Efficient typed numeric storage              |
| `collections.deque`                            | Yes                                              | Yes                        | Yes        | O(1) appends/pops at both ends – queue/stack |
| `queue.Queue`                                  | Yes                                              | Yes                        | Yes        | Thread-safe FIFO (`asyncio.Queue` for async) |
| `heapq` (on a `list`)                          | Partially (heap order)                           | Yes                        | Yes        | Priority queue (min-heap)                    |
| `collections.namedtuple` / `typing.NamedTuple` | Yes                                              | No                         | Yes        | Lightweight records                          |
| `dataclasses.dataclass`                        | –                                                | Yes (`frozen=True` for no) | –          | Typed data containers                        |
| `collections.defaultdict`                      | Insertion                                        | Yes                        | No (keys)  | Dicts with default values                    |
| `collections.Counter`                          | Insertion                                        | Yes                        | No (keys)  | Counting occurrences                         |

Stack → use a `list` (`append`/`pop`). Queue → use `deque` (`list.pop(0)` is O (n)).
Complexities: [Big O](../../computer-science/big-o.md#python-complexities-cheat-sheet).
Only `tuple`, `str`, `frozenset`, `bytes`, numbers, `bool`, `None` and `range` are immutable built-ins.

## Python vs JavaScript

| Data structure    | Python                                              | JavaScript                                           |
|-------------------|-----------------------------------------------------|------------------------------------------------------|
| Array/List        | `list` – mutable ordered sequence `[1, "a", 2.5]`   | `Array` – same                                       |
| Tuple             | `tuple` – immutable `(1, "a", 2.5)`                 | no direct equivalent (`Object.freeze([...])`)        |
| Dictionary/Object | `dict` – mutable, insertion-ordered key-value pairs | `Object` – mutable key-value pairs                   |
| Set               | `set` – mutable, unordered unique values            | `Set` – mutable, **insertion-ordered** unique values |
| Immutable set     | `frozenset`                                         | no direct equivalent                                 |
| Key-value store   | `dict`, `defaultdict`, `OrderedDict`                | `Map` – any key type                                 |

Python is the common choice for data science, scripting and algorithms; JavaScript for web development and async
programming.
Java comparison: [java/overview.md](../java/overview.md#data-structures-java-vs-python).
