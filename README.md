# Python — Algorithms & Data Structures Practice

A curated collection of coding problems solved in Python across LeetCode, HackerRank, CodeSignal, and CoderPad.
Every solution includes **time and space complexity annotations** so you can study and compare approaches at a glance.

---

## Structure

```
Leetcode/
├── algorithms/
│   ├── arrays.py             # Two Sum, Median of Two Sorted Arrays, Sliding Window, …
│   ├── backtracking.py       # Combination Sum, Permutations, Subsets
│   ├── binary_tree.py        # Spiral Matrix, Trapping Rain Water, Combinations
│   ├── bit_manipulation.py   # Chess Board Cell Color, Power of Two
│   ├── dynamic_programming.py# Coin Change, Climbing Stairs, Edit Distance, LCS, …
│   ├── graph_algorithms.py   # Word Ladder, Course Schedule, Design Twitter
│   ├── greedy.py             # Greedy interval and selection problems
│   ├── linked_list.py        # Plus One, Linked List Miscellaneous
│   ├── math_tricks.py        # Math-based problem patterns
│   ├── searching.py          # Binary Search, Power of Two, Add Binary
│   ├── sorting.py            # Sort Colors (Dutch National Flag)
│   └── strings.py            # Reverse Vowels, Valid Parentheses, Gas Station, …
│
├── data_structures/
│   ├── arrays.py             # 4Sum, 3Sum, Product Except Self, Trapping Rain Water, …
│   ├── binary_tree.py        # Spiral Order, Trapping Rain Water, Tree Traversals
│   ├── heap.py               # Meeting Rooms II, Top K Frequent, Median Finder
│   ├── linked_list.py        # Add Two Numbers, Merge Lists, Reverse, Cycle Detection
│   ├── queue.py              # MyQueue, BFS traversals, Rotting Oranges
│   ├── stack.py              # Min Stack, Daily Temperatures, Largest Rectangle
│   ├── strings.py            # Longest Substring, Group Anagrams, Min Window
│   └── trie.py               # Trie / Prefix Tree, Word Search
│
├── math_problems/
│   ├── algebra.py
│   ├── bitwise_math.py
│   ├── combinatorics.py
│   ├── fractions_and_ratios.py
│   ├── geometry.py
│   ├── matrix_ops.py
│   ├── modular_arithmetic.py
│   ├── number_theory.py
│   └── probability.py
│
│   # Standalone problems (named by LC number)
├── two_sum_1.py                      # LC #1
├── add_two_numbers_2.py              # LC #2
├── reverse_integer_7.py              # LC #7
├── palindrome_number_9.py            # LC #9
├── valid_parentheses_20.py           # LC #20
├── best_time_to_buy_and_sell_stock_121.py  # LC #121
├── happy_number_202.py               # LC #202
├── number_of_islands1_200.py         # LC #200
├── search_in_rotated_sorted_array_33.py    # LC #33
├── kth_largest_element_in_an_array_215.py # LC #215
├── first_unique_character_in_a_string_387.py # LC #387
├── pow_x_n_50.py                     # LC #50
├── coin_change_332.py                # LC #322
└── break_palindrome_1328.py          # LC #1328

Hackerrank/
├── algorithms/dynamic_programming.py
├── data_structures/arrays.py
├── data_structures/strings.py
└── (warm-up: arithmetic, loops, conditionals, string ops)

Code Signal/
├── array_manipulation.py
├── lookup_table.py
├── new_prime_num_list.py
├── string_pattern_matching.py
└── two_dimensional_array_traversal.py

Other/           # Classic interview problems
├── balanced_parentheses.py   # Stack-based bracket matching
├── fibonacci.py              # Recursive + DP versions
├── find_missing_number.py    # Gauss formula
├── merge_two_sorted_lists.py # Linked list merge
├── remove_duplicates.py      # Adjacent duplicate removal (stack)
├── reverse_string.py         # Pythonic slice
├── reverse_string_manually.py
└── star_box.py               # Hollow n×n asterisk box

Basics/
└── string_split.py

coderpad/        # CoderPad assessment problems
```

---

## Complexity Format

Every solution follows this annotation style:

```python
# Time: O(n)   — explanation of what n represents and why
# Space: O(n)  — explanation of memory usage
def myFunction(nums):
    ...
```

For class methods, each method gets its own inline tag:

```python
class MinStack:
    # Time: O(1) per op | Space: O(n)
    def push(self, val): ...
    # Time: O(1) | Space: O(1)
    def getMin(self): ...
```

---

## Complexity Quick Reference

| Problem Type | Typical Time | Typical Space |
|---|---|---|
| Hash map lookup (Two Sum) | O(n) | O(n) |
| Two pointers on sorted array | O(n) | O(1) |
| Binary search | O(log n) | O(1) |
| BFS / DFS on graph | O(V + E) | O(V) |
| Backtracking (subsets) | O(n · 2ⁿ) | O(n) |
| 1D dynamic programming | O(n) | O(n) or O(1) |
| 2D dynamic programming | O(m·n) | O(m·n) |
| Heap of size k | O(n log k) | O(k) |
| Merge sort / sort-based | O(n log n) | O(log n) |
| Naive recursion (Fibonacci) | O(2ⁿ) | O(n) |

---

## Languages
Python 3 throughout.
