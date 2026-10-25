# Big O notation

Describes how the running time (or memory – *space complexity*) of an algorithm **grows as the input size grows**. It
gives an upper bound on the growth rate (usually quoted for the worst case; say "average"/"amortized" when that's what
you mean). Related notations: Ω (lower bound), Θ (tight bound).

- Written `O(f(N))`: **O** = "order of", **N** = how much data you have.
- Synonyms: complexity, time complexity, algorithmic complexity, asymptotic complexity.

## Common classes

| Class      | Name        | Examples                                                                                                                             |
|------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------|
| O(1)       | Constant    | Hash-map access/insert/delete by key (average); array index access; push to a linked-list head; peek at heap root; `len(range(...))` |
| O(log N)   | Logarithmic | Binary search (each step halves the search space); heap insert/extract; balanced BST operations                                      |
| O(N)       | Linear      | Looping over an array; searching a linked list; building `list(range(N))`. 10× data → 10× time                                       |
| O(N log N) | Quasilinear | Merge sort, heap sort, quick sort (average; worst case O(N²)), Python's `sorted` (Timsort)                                           |
| O(N²)      | Quadratic   | Insertion, selection and bubble sort; nested loops over the same data. 10× data → 100× time                                          |
| O(2^N)     | Exponential | Naive recursive Fibonacci, subset enumeration                                                                                        |
| O(N!)      | Factorial   | Generating all permutations, brute-force travelling salesman                                                                         |

Also O (N³), O (N^N)… – "as bad as N² is, there's (almost) no upper limit to how horrible your code can get."

## Determining Big O

1. Identify your code.
2. Identify N (e.g. records in the DB, length of the string).
3. Count the steps in a typical run – how does the step count grow with N?
4. Keep the most significant term, drop lower-order terms and coefficients.

Example (from the repo): a loop that scans half the list on average with ~4 steps per iteration costs `2N + 1` → **O (
N)**;
calling that linear function once per element of a list makes it `N² + kN + 1` → **O (N²)**.

```python
def find_mom(child):
    for mom_name, child_name in moms:   # up to N iterations
        if child == child_name:
            return mom_name
    return None                          # O(N)

def grandmothers_count():
    count = 0
    for child, mom in moms:              # N
        if find_mom(mom):                # N each → O(N²) overall
            count += 1
    return count
```

Source: [`examples/python/bigO`](../../examples/python/bigO)

## Python complexities (cheat sheet)

| Lists          |            | Dicts          |      | Sets         |      |
|----------------|------------|----------------|------|--------------|------|
| `append`       | O(1)       | `d[key] = val` | O(1) | `s.add(x)`   | O(1) |
| `lst[i]`       | O(1)       | `d[key]`       | O(1) | `x in s`     | O(1) |
| `x in lst`     | **O(N)**   | `key in d`     | O(1) | `for x in s` | O(N) |
| `for x in lst` | O(N)       | `for k in d`   | O(N) |              |      |
| `lst.sort()`   | O(N log N) |                |      |              |      |

Pro-tip: replace lists with sets/dicts when you mostly test membership.

## Small numbers

> "Fancy algorithms are slow when n is small, and n is usually small." – Rob Pike

In other words, avoid premature optimization: measure first.

## Resources

- Ned Batchelder – [Big-O: How Code Slows as Data Grows (PyCon 2018)](https://www.youtube.com/watch?v=duvZ-2UK0fc)
- [Python Big O: time complexities of Python data structures](https://www.pythonmorsels.com/time-complexities/)

Related: [data structures](data-structures.md), [algorithms](algorithms.md).
