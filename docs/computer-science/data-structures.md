# Data structures

Organized ways of storing and managing data so operations on it (search, insert, delete) are efficient: containers +
rules
for how data is arranged.

## 1. Arrays

Contiguous block of memory of same-typed elements (low-level languages). Python's `list` behaves like a dynamic array.

- **Purpose:** fast random access by index, sequential data, foundation for heaps/hash tables.
- **Pros:** O (1) access, memory-efficient, cache-friendly.
- **Cons:** insert/delete in the middle is slow (shifting), fixed size in low-level languages, resizing is expensive
  (amortized O (1) append).

## 2. Linked lists

Chain of nodes, each with data + pointer to next (and maybe previous).

- **Purpose:** frequent insert/delete; used in queues, adjacency lists, memory allocators.
- **Pros:** O (1) insert/delete if you hold the node, flexible size, no reallocation.
- **Cons:** O (n) search, poor cache locality, pointer overhead.

## 3. Stacks (LIFO)

Push/pop on one end. **Purpose:** recursion (call stack), undo/redo, expression parsing, DFS. **Pros:** simple, O (1)
push/pop. **Cons:** no random access, LIFO only.

## 4. Queues (FIFO)

Elements enter at the back, leave from the front. **Purpose:** scheduling, message brokers, BFS, buffers. **Pros:** O
(1) enqueue/dequeue (linked list / ring buffer / Python `collections.deque` – *not* `list.pop(0)`, which is
O (n)). **Cons:** no random access, FIFO only.

## 5. Hash tables (maps / dicts)

Key→value storage using hashing (Python `dict`, JS `Map`, Java `HashMap`). **Purpose:** fast lookups, caches, sets,
config.

- **Pros:** O (1) average search/insert/delete, flexible keys, built-in almost everywhere.
- **Cons:** O (n) worst case (collisions), more memory, iteration order depends on the implementation (insertion-ordered
  in Python ≥3.7, JS `Map`, Java `LinkedHashMap`; not in Java `HashMap`).

## 6. Trees

Hierarchical nodes (parent → children). **Purpose:** filesystems, DOM, org structures; basis for BST, heaps, tries.
**Pros:** good for hierarchical/ordered data, efficient search if balanced. **Cons:** more complex, need balancing for
log-time operations.

## 7. Binary search trees (BST)

Each node has ≤2 children; left < node < right. **Purpose:** ordered data access, range queries, ordered maps/sets (Java
`TreeMap`, C++ `std::map` use red-black trees; Python `dict`/`set` do **not** – they're hash tables). **Pros:** O (log
n) if balanced, keeps sorted order. **Cons:** degrades to O (n) if unbalanced; balancing (AVL/red-black
rotations) is harder to implement.

## 8. Heaps (priority queue)

Complete binary tree where each parent is ≤ (min-heap) or ≥ (max-heap) its children. **Purpose:** get min/max fast,
schedulers, Dijkstra, timers/rate limiters. **Pros:** O (1) peek, O (log n) insert and extract, simple array
implementation. **Cons:** no random access, search is
O (n), only the top element is cheap to get (arbitrary delete is O (n) unless you track positions).

## 9. Graphs

Vertices + edges. **Purpose:** networks, social graphs, routing, dependencies, workflows. **Pros:** extremely flexible.
**Cons:** harder to implement correctly; algorithms depend on size (BFS/DFS cost O (V+E); all-pairs shortest paths
Floyd–Warshall O (V³)).

### DFS and BFS

- **DFS – Depth-First Search:** go deep along one path before backtracking; uses a stack (or recursion). Good for
  path finding, topological sort, cycle detection, backtracking problems.
- **BFS – Breadth-First Search:** explore neighbors level by level; uses a queue. Good for shortest path in unweighted
  graphs, level-order traversal, minimum steps.

## Time complexity comparison

| Data structure   | Access   | Search   | Insert   | Delete    |
|------------------|----------|----------|----------|-----------|
| Array            | O(1)     | O(n)     | O(n)     | O(n)      |
| Linked list      | O(n)     | O(n)     | O(1)¹    | O(1)¹     |
| Stack            | O(n)     | O(n)     | O(1)     | O(1)      |
| Queue            | O(n)     | O(n)     | O(1)     | O(1)      |
| Hash table       | O(1)²    | O(1)²    | O(1)²    | O(1)²     |
| BST (balanced)   | O(log n) | O(log n) | O(log n) | O(log n)  |
| BST (unbalanced) | O(n)     | O(n)     | O(n)     | O(n)      |
| Heap             | O(n)     | O(n)     | O(log n) | O(log n)³ |
| Graph            | –        | O(V+E)   | varies   | varies    |

¹ Only when you already hold the node reference; finding the spot is O (n).
² Average case; O (n) worst case because of collisions.
³ Extract-min/max. Peek at the top is O (1).

Related: [Big O](big-o.md), [algorithms](algorithms.md), [Python data structures](../languages/python/data-structures.md),
[Java vs Python](../languages/java/overview.md#data-structures-java-vs-python).
