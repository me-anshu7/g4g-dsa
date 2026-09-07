# g4g-dsa

Practice code, implementations, and notes from the GeeksforGeeks DSA course, implemented in Python.

---

## 📁 Repository Structure & Naming Conventions

To keep the codebase organized, clean, and adhering to [PEP 8](https://peps.python.org/pep-0008/) standards, the following conventions are used across this repository.

### 1. Folder Naming (Topics & Modules)

Topic folders follow **`lowercase_snake_case`**, with an optional two-digit numerical prefix to preserve the chronological order of the GeeksforGeeks course syllabus:

* `01_mathematics/`
* `02_bit_magic/`
* `03_recursion/`
* `04_arrays/`
* `05_searching/`
* `06_sorting/`
* `07_matrix/`
* `08_hashing/`
* `09_strings/`
* `10_linked_list/`
* `11_stack/`
* `12_queue/`
* `13_trees/`
* `14_binary_search_tree/`
* `15_heap/`
* `16_graph/`
* `17_greedy/`
* `18_backtracking/`
* `19_dynamic_programming/`

---

### 2. File Naming Conventions

#### **Python Files (`.py`)**
* Always use **`snake_case`** (lowercase letters with underscores).
* Do **not** use hyphens (`-`) or spaces in filenames, as they prevent standard Python imports and violate PEP 8.
* Examples:
  * `count_digits.py`
  * `palindrome_number.py`
  * `trailing_zeros_in_factorial.py`
  * `gcd_euclidean.py`
  * `sieve_of_eratosthenes.py`
* *(Optional)* If keeping chronological order within a topic:
  * `01_count_digits.py`
  * `02_palindrome_number.py`

#### **Documentation & Notes (`.md`)**
* `README.md` for folder-level notes, problem indexes, or formula reference.
* `notes.md` or `cheatsheet.md` for personal study notes and key takeaways.

---

### 3. File Template & Code Structure

Each solution file should follow a clean structure including problem details, complexities, type hints, and self-contained test cases:

```python
"""
Problem: Trailing Zeros in Factorial
Description: Count trailing zeros in n! efficiently.
Time Complexity: O(log5(n))
Space Complexity: O(1)
"""

def count_trailing_zeros(n: int) -> int:
    count = 0
    i = 5
    while n >= i:
        count += n // i
        i *= 5
    return count


if __name__ == "__main__":
    # Test cases / Driver code
    assert count_trailing_zeros(10) == 2
    assert count_trailing_zeros(100) == 24
    print("All tests passed!")
```

---

### 4. Directory Tree Example

```text
g4g-dsa/
├── README.md
├── 01_mathematics/
│   ├── README.md                          # (Optional) Topic notes / formula reference
│   ├── count_digits.py
│   ├── palindrome_number.py
│   ├── trailing_zeros_in_factorial.py
│   ├── gcd_lcm.py
│   ├── check_for_prime.py
│   └── sieve_of_eratosthenes.py
├── 02_bit_magic/
│   ├── check_kth_bit_set.py
│   └── count_set_bits.py
└── 03_recursion/
    ├── print_1_to_n.py
    └── rope_cutting_problem.py
```
