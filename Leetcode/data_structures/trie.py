# LeetCode - Trie Problems
# Collection of trie-based problems from LeetCode

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# TRIE PROBLEMS
# =============================================================================

# PROBLEM: Implement Trie (LC 208)
# Goal: Implement a trie (prefix tree) with insert, search, and startsWith operations
# This uses a tree structure where each node has children for each character
# Pseudocode:
#   1. Each node has children dictionary and is_end flag
#   2. Insert: traverse/create path, mark end node
#   3. Search: traverse path, check if end node exists
#   4. startsWith: traverse path, return True if path exists
# Time: O(1) | Space: O(1)
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    # Time: O(m) | Space: O(m)
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True
    
    # Time: O(m) | Space: O(1)
    def search(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    # Time: O(m) | Space: O(1)
    def startsWith(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
