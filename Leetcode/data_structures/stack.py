# LeetCode - Stack Problems
# Collection of stack-based problems from LeetCode

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# STACK PROBLEMS
# =============================================================================

# PROBLEM: Min Stack (LC 155)
# Goal: Design a stack that supports push, pop, top, and getMin in O(1) time
# This uses two stacks: one for values, one for minimums
# Pseudocode:
#   1. Use two stacks: one for values, one for minimums
#   2. When pushing: add to both stacks, min stack gets min(current, top of min stack)
#   3. When popping: pop from both stacks
#   4. getMin returns top of min stack
# Time: O(1) per op | Space: O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    # Time: O(1) | Space: O(1)
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    # Time: O(1) | Space: O(1)
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    # Time: O(1) | Space: O(1)
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
