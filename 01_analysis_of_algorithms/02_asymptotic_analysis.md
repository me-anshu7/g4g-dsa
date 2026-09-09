# 02. Asymptotic Analysis & Order of Growth

## 1. What is Asymptotic Analysis?
Asymptotic analysis evaluates how the **runtime of an algorithm grows as the input size (`n`) increases**.
- Terms like **Big-O ($O$)**, **Theta ($\Theta$)**, and **Omega ($\Omega$)** are known as asymptotic notations.
- It is **machine-independent**, **language-independent**, and evaluated theoretically before implementing any code.

---

## 2. Expressing Time in Terms of Input Size (`n`)

### Core Assumption
Any single basic operation (arithmetic calculation, comparison, assignment) is assumed to take **constant time**, regardless of input value size.

### Revisiting the Sum of First `n` Numbers:
| Function | Operations Breakdown | Time Expression | Order of Growth |
| :--- | :--- | :--- | :--- |
| **`fun1` (Formula)** | 3 operations (add, multiply, divide) | `C1` | **Constant** |
| **`fun2` (Single Loop)** | Loop body runs `n` times + initial setup | `C2*n + C3` | **Linear** |
| **`fun3` (Nested Loops)** | Inner loop runs `n*(n+1)/2` times | `C4*n^2 + C5*n + C6` | **Quadratic** |

> **Rule of Thumb:** In asymptotic analysis, we **drop the constants and lower-order terms**, keeping only the leading (highest order) term.

---

## 3. Why Order of Growth Beats Machine Speed

Even if an inefficient algorithm is executed on a supercomputer and an efficient algorithm on a slow machine, **the algorithm with lower order of growth will always win for sufficiently large `n`**.

### Example 1: Constant vs Linear
* **`fun1` (Constant)** on slow machine: `T1 = 13`
* **`fun2` (Linear)** on faster machine: `T2 = 2*n + 5`
* **Intersection point:** `13 = 2*n + 5` $\rightarrow$ `n = 4`
* **Result:** For any `n > 4`, `fun2` is **always slower**, regardless of its faster hardware.

### Example 2: Extreme Constant vs Linear
* **`fun1` (Constant)** on a mobile phone: `T1 = 1000`
* **`fun2` (Linear)** on a supercomputer: `T2 = n + 1`
* **Intersection point:** `n = 999`
* **Result:** For any `n > 999`, the linear solution on the supercomputer takes **more time** than the constant solution on a phone.

---

## 4. Key Takeaways
1. **Lower order of growth always wins** once `n` passes a certain threshold (intersection point).
2. **Quadratic ($n^2$) grows far faster than Linear ($n$)**, which grows far faster than Constant ($1$).
3. **Quadrant 1 Only:** Since input size `n >= 0` and runtime `T >= 0`, all asymptotic graphs live exclusively in the first quadrant of the coordinate system.
