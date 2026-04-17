# Python -- Algorithms and Data Structures

Coding problems in Python across LeetCode, HackerRank, CodeSignal, and CoderPad. Every solution has time and space complexity annotations so the tradeoffs are explicit.

## Structure

```
Leetcode/
├── algorithms/
│   ├── arrays.py              # Two Sum, Median of Two Sorted Arrays, Sliding Window
│   ├── backtracking.py        # Combination Sum, Permutations, Subsets
│   ├── binary_tree.py         # Spiral Matrix, Trapping Rain Water, Combinations
│   ├── bit_manipulation.py    # Chess Board Cell Color, Power of Two
│   ├── dynamic_programming.py # Coin Change, Climbing Stairs, Edit Distance, LCS
│   ├── graph_algorithms.py    # Word Ladder, Course Schedule, Design Twitter
│   ├── greedy.py              # Greedy interval and selection problems
│   ├── linked_list.py         # Plus One, linked list miscellaneous
│   ├── math_tricks.py         # Math-based problem patterns
│   ├── searching.py           # Binary Search, Power of Two, Add Binary
│   ├── sorting.py             # Sort Colors (Dutch National Flag)
│   └── strings.py             # Reverse Vowels, Valid Parentheses, Gas Station
│
├── data_structures/
│   ├── arrays.py              # 4Sum, 3Sum, Product Except Self, Trapping Rain Water
│   ├── binary_tree.py         # Spiral Order, Trapping Rain Water, Tree Traversals
│   ├── heap.py                # Meeting Rooms II, Top K Frequent, Median Finder
│   ├── linked_list.py         # Add Two Numbers, Merge Lists, Reverse, Cycle Detection
│   ├── queue.py               # MyQueue, BFS traversals, Rotting Oranges
│   ├── stack.py               # Min Stack, Daily Temperatures, Largest Rectangle
│   ├── strings.py             # Longest Substring, Group Anagrams, Min Window
│   └── trie.py                # Trie / Prefix Tree, Word Search
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
├── two_sum_1.py
├── add_two_numbers_2.py
├── reverse_integer_7.py
├── palindrome_number_9.py
├── valid_parentheses_20.py
├── search_in_rotated_sorted_array_33.py
├── pow_x_n_50.py
├── best_time_to_buy_and_sell_stock_121.py
├── happy_number_202.py
├── number_of_islands1_200.py
├── kth_largest_element_in_an_array_215.py
├── coin_change_332.py
├── first_unique_character_in_a_string_387.py
└── break_palindrome_1328.py

Hackerrank/
├── algorithms/dynamic_programming.py
├── data_structures/arrays.py
├── data_structures/strings.py
└── warm-up problems: arithmetic, loops, conditionals, string ops

Code Signal/
├── array_manipulation.py
├── lookup_table.py
├── new_prime_num_list.py
├── string_pattern_matching.py
└── two_dimensional_array_traversal.py

Other/           # Classic interview problems
├── balanced_parentheses.py    # Stack-based bracket matching
├── fibonacci.py               # Recursive version
├── find_missing_number.py     # Gauss formula
├── merge_two_sorted_lists.py  # Linked list merge
├── remove_duplicates.py       # Adjacent duplicate removal via stack
├── reverse_string.py          # Pythonic slice
├── reverse_string_manually.py
└── star_box.py                # Hollow n x n asterisk box

Basics/
└── string_split.py

coderpad/        # CoderPad assessment problems
```

## Complexity annotations

Every solution is annotated like this:

```python
# Time: O(n)   -- single pass through the array
# Space: O(n)  -- hash map stores at most n elements
def twoSum(self, nums, target):
    ...
```

For classes, each method gets its own tag:

```python
class MinStack:
    # Time: O(1) per op | Space: O(n)
    def push(self, val): ...
    # Time: O(1) | Space: O(1)
    def getMin(self): ...
```

## Quick reference

| Problem type | Time | Space |
|---|---|---|
| Hash map lookup | O(n) | O(n) |
| Two pointers on sorted array | O(n) | O(1) |
| Binary search | O(log n) | O(1) |
| BFS / DFS | O(V + E) | O(V) |
| Backtracking (subsets) | O(n * 2^n) | O(n) |
| 1D dynamic programming | O(n) | O(n) or O(1) |
| 2D dynamic programming | O(m*n) | O(m*n) |
| Heap of size k | O(n log k) | O(k) |
| Merge sort | O(n log n) | O(log n) |
| Naive recursion (Fibonacci) | O(2^n) | O(n) |

## Language

Python 3
