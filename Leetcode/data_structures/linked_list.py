# LeetCode - Linked List Problems
# Collection of linked list problems from LeetCode

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# CLASS DEFINITIONS
# =============================================================================

# ListNode class for linked list problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# =============================================================================
# LINKED LIST PROBLEMS
# =============================================================================

# PROBLEM: Add Two Numbers (LC 2)
# Goal: Add two numbers represented as linked lists (digits in reverse order)
# This is like elementary school addition but with linked lists!
# Pseudocode:
#   1. Create dummy node for result
#   2. Keep track of carry
#   3. Add digits from both lists plus carry
#   4. Create new node with sum % 10
#   5. Update carry = sum // 10
#   6. Continue until both lists are exhausted and carry is 0
# Time: O(max(m,n)), Space: O(max(m,n))
def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # Dummy node to simplify logic
    current = dummy  # Current pointer for building result
    carry = 0  # Track carry from previous addition
    while l1 or l2 or carry:  # While there are digits or carry left
        sum_val = carry  # Start with carry
        if l1:  # If l1 has digits left
            sum_val += l1.val  # Add l1's digit
            l1 = l1.next  # Advance l1
        if l2:  # If l2 has digits left
            sum_val += l2.val  # Add l2's digit
            l2 = l2.next  # Advance l2
        carry = sum_val // 10  # Calculate new carry
        current.next = ListNode(sum_val % 10)  # Create node with ones digit
        current = current.next  # Advance result pointer
    return dummy.next  # Return actual head

# PROBLEM: Merge Two Sorted Lists (LC 21)
# Goal: Merge two sorted linked lists into one sorted list
# This uses the classic merge technique from merge sort!
# Pseudocode:
#   1. Create a dummy node to simplify edge cases
#   2. Compare nodes from both lists
#   3. Attach smaller node to result and advance that list's pointer
#   4. When one list is exhausted, attach remaining list
#   5. Return dummy.next (the actual head of merged list)
# Time: O(n + m), Space: O(1)
def mergeTwoLists(l1, l2):
    dummy = ListNode(0)  # Dummy node to simplify logic
    current = dummy  # Current pointer for building result
    while l1 and l2:  # While both lists have nodes
        if l1.val <= l2.val:  # If l1's value is smaller
            current.next = l1  # Attach l1's node
            l1 = l1.next  # Advance l1
        else:  # If l2's value is smaller
            current.next = l2  # Attach l2's node
            l2 = l2.next  # Advance l2
        current = current.next  # Advance result pointer
    current.next = l1 or l2  # Attach remaining nodes
    return dummy.next  # Return actual head

# PROBLEM: Reverse Linked List (LC 206)
# Goal: Reverse a singly linked list iteratively
# This is a classic iterative reversal using three pointers!
# Pseudocode:
#   1. Use three pointers: prev, current, next
#   2. For each node, reverse its next pointer
#   3. Move all pointers one step forward
#   4. Continue until we reach the end
#   5. Return prev (new head)
# Time: O(n), Space: O(1)
def reverseList(head):
    prev = None  # Previous node (will become new head)
    current = head  # Current node being processed
    while current:  # While there are nodes left
        next_temp = current.next  # Save next node
        current.next = prev  # Reverse the pointer
        prev = current  # Move prev forward
        current = next_temp  # Move current forward
    return prev  # Return new head
