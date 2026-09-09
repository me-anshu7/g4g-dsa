# 01. Introduction to Analysis of Algorithms

## 1. Why Analysis of Algorithms?
For any computational problem, there can be multiple solutions using different algorithmic paradigms and data structures. **Analysis of algorithms** provides a systematic way to evaluate and compare these solutions to decide which one is most efficient.

---

## 2. Motivating Example: Sum of First `n` Natural Numbers
Given an integer `n`, find the sum: `1 + 2 + 3 + ... + n`.

### Three Approaches
| Solution | Approach | Logic / Code Concept |
| :--- | :--- | :--- |
| **Solution 1** | Mathematical Formula | `return n * (n + 1) // 2` |
| **Solution 2** | Single Loop | Loop from `1` to `n`, adding `i` to `sum` |
| **Solution 3** | Nested Loops | Outer loop `1` to `n`, inner loop `1` to `i`, incrementing `sum += 1` |

> All three approaches produce the exact same correct result, but their efficiency differs drastically.

---

## 3. Why Measuring Real Execution Time (Wall Clock) Fails
Directly timing a program (e.g., using a stopwatch or `time()` function) is **not** a reliable way to compare algorithms because:

1. **Machine Hardware Differences**: An inefficient algorithm on a fast machine can run quicker than an efficient algorithm on a slow machine.
2. **Programming Language**: Compiled languages (C / C++) generate native machine binaries and run faster than interpreted / intermediate languages (Python / Java).
3. **System Load**: Background OS updates, other running apps, and CPU throttling distort execution times.
4. **Input Size Variance**: One algorithm might be slightly faster for small `n`, but drastically slower when `n` grows large.

---

## 4. The Solution: Asymptotic Analysis
To overcome physical machine dependencies, computer science uses **Asymptotic Analysis**:
* **Theoretical & Mathematical**: Evaluates algorithms on paper without needing to run or benchmark them on hardware.
* **Hardware & Language Independent**: Focuses solely on how the number of operations scales as input size (`n`) approaches infinity.
* **Order of Growth**: Allows programmers to definitively determine which algorithm scales better.
