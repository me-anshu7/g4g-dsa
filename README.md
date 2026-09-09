# g4g-dsa

Practice code, implementations, and notes from the GeeksforGeeks DSA course, implemented in Python.

---

## 📁 Repository Structure & Naming Conventions

To keep the codebase organized, clean, and adhering to [PEP 8](https://peps.python.org/pep-0008/) standards, the following conventions are used across this repository.

### 1. Folder Naming (Topics & Modules)

Topic folders follow **`lowercase_snake_case`**, with a two-digit numerical prefix preserving the chronological order of the GeeksforGeeks course syllabus:

* `01_analysis_of_algorithms/`
* `02_mathematics/`
* `03_bit_magic/`
* `04_recursion/`
* `05_arrays/`
* `06_searching/`
* `07_sorting/`
* `08_matrix/`
* `09_hashing/`
* `10_strings/`
* `11_linked_list/`
* `12_stack/`
* `13_queue/`
* `14_trees/`
* `15_binary_search_tree/`
* `16_heap/`
* `17_graph/`
* `18_greedy/`
* `19_backtracking/`
* `20_dynamic_programming/`

---

### 2. File Naming Conventions

#### **Python Files (`.py`)**
* Always use **`lowercase_snake_case`** with a two-digit numerical prefix to maintain chronological order within each topic:
  * `01_count_digits.py`
  * `02_absolute_value.py`
  * `03_convert_celsius_to_fahrenheit.py`
  * `04_factorial_of_number.py`
* Do **not** use hyphens (`-`) or spaces in filenames, as they prevent standard Python imports and violate PEP 8.

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
├── 01_analysis_of_algorithms/
│   ├── README.md                                # Chapter index / Table of Contents
│   ├── 01_introduction_to_analysis_of_algorithms.md
│   ├── 02_asymptotic_analysis.md
│   └── ...
├── 02_mathematics/
│   ├── README.md                                # (Optional) Topic notes / formula reference
│   ├── 01_count_digits.py
│   ├── 02_absolute_value.py
│   ├── 03_convert_celsius_to_fahrenheit.py
│   ├── 04_factorial_of_number.py
│   └── ...
├── 03_bit_magic/
│   ├── 01_check_kth_bit_set.py
│   └── 02_count_set_bits.py
└── 04_recursion/
    ├── 01_print_1_to_n.py
    └── 02_rope_cutting_problem.py
```
