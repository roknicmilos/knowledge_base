# Java overview

High-level, object-oriented, platform-independent language and platform, first released by Sun Microsystems in 1995 (now
Oracle). Used for enterprise applications, web servers and big-data systems; Android supports Java, but Kotlin is
Google's preferred language there.

## How Java works

1. Write code → save as `.java` (e.g. `HelloWorld.java`).
2. Compile → `javac HelloWorld.java` → `.class` bytecode.
3. Run → `java HelloWorld` – the JVM executes the bytecode. (Since Java 11 you can also run a single source file
   directly: `java HelloWorld.java`.)

## Java vs other languages

| Feature           | Java                          | Python                         | C++                | JavaScript           |
|-------------------|-------------------------------|--------------------------------|--------------------|----------------------|
| Typing            | Static                        | Dynamic                        | Static             | Dynamic              |
| Speed             | Fast (JIT-optimized)          | Slower (interpreted bytecode)  | Very fast          | Moderate (JIT in V8) |
| Typical use       | Enterprise, backend, big data | Scripting, AI/ML               | System programming | Web                  |
| Memory management | Garbage collection            | Reference counting + cyclic GC | Manual             | Garbage collection   |

**Pros:** platform-independent (JVM runs everywhere), high performance (JIT), strong community and ecosystem, secure and
stable. **Cons:** verbose syntax, slower start-up (JVM warm-up), memory-heavy.

## Data structures: Java vs Python

| Category              | Java                                                         | Python                                                                | Immutable? | Notes                                                         |
|-----------------------|--------------------------------------------------------------|-----------------------------------------------------------------------|------------|---------------------------------------------------------------|
| Dynamic array         | `ArrayList<E>`                                               | `list`                                                                | No         | Python lists are heterogeneous; Java generics are homogeneous |
| Immutable sequence    | `List.of()` (Java 9+)                                        | `tuple`                                                               | Yes        | Python built-in; Java factory method                          |
| Linked list           | `LinkedList<E>`                                              | `collections.deque` (block-linked list)                               | No         | Both support queue operations                                 |
| Hash table            | `HashMap<K,V>`                                               | `dict`                                                                | No         | Python: any hashable key; Java: `hashCode()`/`equals()`       |
| Insertion-ordered map | `LinkedHashMap<K,V>`                                         | `dict` (ordered since 3.7; `OrderedDict` only for `move_to_end` etc.) | No         |                                                               |
| Set                   | `HashSet<E>`                                                 | `set`                                                                 | No         |                                                               |
| Insertion-ordered set | `LinkedHashSet<E>`                                           | `dict.fromkeys(...)` (no real ordered set)                            | No         |                                                               |
| Stack                 | `ArrayDeque<E>` (legacy `Stack<E>` is synchronized and slow) | `list` (`append`/`pop`)                                               | No         |                                                               |
| FIFO queue            | `ArrayDeque<E>`, `LinkedList<E>`                             | `collections.deque`; `queue.Queue` (thread-safe)                      | No         |                                                               |
| Priority queue / heap | `PriorityQueue<E>` (custom comparators)                      | `heapq` (min-heap on a list)                                          | No         |                                                               |
| String                | `String` (immutable, UTF-16)                                 | `str` (immutable, Unicode)                                            | Yes        | Python: slicing; Java: `substring()`                          |
| Primitive arrays      | `int[]`                                                      | `array.array` (rarely used)                                           | No         | Java arrays are fast but fixed-size                           |

Key insights:

- **Immutability:** Python immutable built-ins: `tuple`, `str`, `frozenset`, `bytes`, numbers, `bool`, `None`, `range`.
  Java: `List.of()`, `String`, records (Java 16+, shallowly immutable).
- **Philosophy:** Python optimizes for flexibility (mixed types, concise syntax); Java for performance and type safety.
- Equivalents: `list` ↔ `ArrayList`, `tuple` ↔ `List.of()`, `dict` ↔ `HashMap`.
- Choose Python for quick prototyping/scripting/mixed data; Java for large systems, performance-critical or strictly
  typed code.

Related: [data structures](../../computer-science/data-structures.md), [Python data
structures](../python/data-structures.md).
