# Binary Tree Problems
# Collection of binary tree problems from LeetCode, CodeSignal, and other platforms

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# CLASS DEFINITIONS
# =============================================================================

# TreeNode class for binary tree problems
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# =============================================================================
# BINARY TREE PROBLEMS
# =============================================================================

# PROBLEM: Level Order Traversal II (LC 107)
# Goal: Return level order traversal from bottom to top
# This is same as level order but reversed at the end
# Pseudocode:
#   1. Perform normal level order traversal (BFS)
#   2. Store each level in result array
#   3. Reverse the result array before returning
def levelOrderBottom(root):
   if not root:  # Edge case: empty tree
       return []
   result = []  # Store levels
   queue = [root]  # BFS queue
   while queue:  # Process each level
       level_size = len(queue)  # Number of nodes in current level
       level = []  # Current level values
       for _ in range(level_size):  # Process all nodes in current level
           node = queue.pop(0)  # Get next node
           level.append(node.val)  # Add value to level
           if node.left:  # Add left child
               queue.append(node.left)
           if node.right:  # Add right child
               queue.append(node.right)
       result.append(level)  # Add level to result
   return result[::-1]  # Return reversed result (bottom to top)

# PROBLEM: Convert Sorted Array to Binary Search Tree (LC 108) - Import: TreeNode
# Goal: Convert sorted array to height-balanced BST
# This uses recursive approach with middle element as root
# Pseudocode:
#   1. Base case: empty array returns None
#   2. Choose middle element as root
#   3. Recursively build left subtree with left half
#   4. Recursively build right subtree with right half
def sortedArrayToBST(nums):
   if not nums:  # Base case: empty array
       return None
   mid = len(nums) // 2  # Find middle index
   root = TreeNode(nums[mid])  # Create root with middle element
   root.left = sortedArrayToBST(nums[:mid])  # Build left subtree with left half
   root.right = sortedArrayToBST(nums[mid+1:])  # Build right subtree with right half
   return root

# PROBLEM: Convert Sorted List to Binary Search Tree (LC 109) - Import: ListNode, TreeNode
# Goal: Convert sorted linked list to height-balanced BST
# This converts list to array first, then builds BST
# Pseudocode:
#   1. Convert linked list to array
#   2. Use recursive approach with middle element as root
#   3. Build left and right subtrees recursively
def sortedListToBST(head):
   if not head:  # Edge case: empty list
       return None
   # Convert linked list to array
   nums = []  # Store values in array
   current = head
   while current:  # Traverse linked list
       nums.append(current.val)  # Add value to array
       current = current.next  # Move to next node
   def buildBST(left, right):  # Helper: build BST from array range
       if left > right:  # Base case: invalid range
           return None
       mid = (left + right) // 2  # Find middle index
       root = TreeNode(nums[mid])  # Create root with middle element
       root.left = buildBST(left, mid - 1)  # Build left subtree
       root.right = buildBST(mid + 1, right)  # Build right subtree
       return root
   return buildBST(0, len(nums) - 1)  # Build BST from entire array

# PROBLEM: Balanced Binary Tree (LC 110) - Import: TreeNode
# Goal: Check if binary tree is height-balanced (heights of subtrees differ by at most 1)
# This uses recursive height calculation with early termination
# Pseudocode:
#   1. Calculate height of each subtree recursively
#   2. If any subtree is unbalanced, return -1
#   3. Check if height difference > 1, return -1 if so
#   4. Return height if balanced, -1 if not
# Time: O(n) | Space: O(h)
def isBalanced(root):
   def getHeight(node):  # Helper: get height and check balance
       if not node:  # Base case: null node has height 0
           return 0
       left_height = getHeight(node.left)  # Get left subtree height
       if left_height == -1:  # If left subtree unbalanced
           return -1  # Propagate unbalance
       right_height = getHeight(node.right)  # Get right subtree height
       if right_height == -1:  # If right subtree unbalanced
           return -1  # Propagate unbalance
       if abs(left_height - right_height) > 1:  # If height difference > 1
           return -1  # Tree is unbalanced
       return 1 + max(left_height, right_height)  # Return height of current node
   return getHeight(root) != -1  # Tree is balanced if height != -1

# PROBLEM: Binary Tree Maximum Path Sum (LC 124) - Import: TreeNode
# Goal: Find maximum path sum in binary tree
# Time: O(n), Space: O(h) where h is height of tree
# Pseudocode:
#   1. Use DFS to calculate max gain from each node
#   2. For each node, calculate path sum including left and right subtrees
#   3. Update global maximum
#   4. Return max gain going through current node
# Time: O(n) | Space: O(h)
def maxPathSum(root):
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        current_path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path_sum)
        
        return node.val + max(left_gain, right_gain)
    
    max_sum = float('-inf')
    max_gain(root)
    return max_sum

# PROBLEM 1: Maximum Depth of Binary Tree (LC 104)
# Goal: Find maximum depth of binary tree
# Time: O(n), Space: O(h) where h is height of tree
# Pseudocode:
#   1. Base case: if root is None, return 0
#   2. Recursively find depth of left and right subtrees
#   3. Return 1 + max(left_depth, right_depth)
# Time: O(n) | Space: O(h)
def maxDepth(root):
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# PROBLEM 2: Symmetric Tree (LC 101)
# Goal: Check if binary tree is symmetric
# Time: O(n), Space: O(h) where h is height of tree
# Pseudocode:
#   1. Helper function to check if two trees are mirror images
#   2. Compare left subtree of one with right subtree of other
#   3. Compare right subtree of one with left subtree of other
# Time: O(n) | Space: O(h)
def isSymmetric(root):
    if not root:
        return True
    
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    return is_mirror(root.left, root.right)

# PROBLEM 3: Binary Tree Level Order Traversal (LC 102)
# Goal: Return level order traversal of binary tree
# Time: O(n), Space: O(w) where w is maximum width of tree
# Pseudocode:
#   1. Use BFS with queue
#   2. Process nodes level by level
#   3. For each level, collect all node values
# Time: O(n) | Space: O(n)
def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# PROBLEM 4: Binary Tree Zigzag Level Order Traversal (LC 103)
# Goal: Return zigzag level order traversal
# Time: O(n), Space: O(w) where w is maximum width of tree
# Pseudocode:
#   1. Use BFS with queue
#   2. Alternate direction for each level
#   3. Reverse level when going right to left
def zigzagLevelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if not left_to_right:
            level.reverse()
        
        result.append(level)
        left_to_right = not left_to_right
    
    return result

# PROBLEM 5: Path Sum (LC 112)
# Goal: Check if there's a root-to-leaf path with given sum
# Time: O(n), Space: O(h) where h is height of tree
# Pseudocode:
#   1. Base case: if root is None, return False
#   2. If leaf node, check if value equals remaining sum
#   3. Recursively check left and right subtrees
# Time: O(n) | Space: O(h)
def hasPathSum(root, targetSum):
    if not root:
        return False
    
    if not root.left and not root.right:  # Leaf node
        return root.val == targetSum
    
    remaining = targetSum - root.val
    return (hasPathSum(root.left, remaining) or 
            hasPathSum(root.right, remaining))

# PROBLEM 6: Binary Tree Maximum Path Sum (LC 124)
# Goal: Find maximum path sum in binary tree
# Time: O(n), Space: O(h) where h is height of tree
# Pseudocode:
#   1. Use DFS to calculate max gain from each node
#   2. For each node, calculate path sum including left and right subtrees
#   3. Update global maximum
# Time: O(n) | Space: O(h)
def maxPathSum(root):
    max_sum = float('-inf')
    
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # Max gain from left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Current path sum including this node
        current_path_sum = node.val + left_gain + right_gain
        
        # Update global maximum
        max_sum = max(max_sum, current_path_sum)
        
        # Return max gain for parent
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum

# PROBLEM 7: Construct Binary Tree from Preorder and Inorder Traversal (LC 105)
# Goal: Build binary tree from preorder and inorder traversals
# Time: O(n), Space: O(n)
# Pseudocode:
#   1. First element in preorder is root
#   2. Find root position in inorder
#   3. Left subtree: preorder[1:root_pos+1], inorder[:root_pos]
#   4. Right subtree: preorder[root_pos+1:], inorder[root_pos+1:]
# Time: O(n) | Space: O(n)
def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    root_index = inorder.index(root_val)
    
    root.left = buildTree(preorder[1:root_index+1], inorder[:root_index])
    root.right = buildTree(preorder[root_index+1:], inorder[root_index+1:])
    
    return root

# PROBLEM 8: Serialize and Deserialize Binary Tree (LC 297)
# Goal: Serialize tree to string and deserialize string back to tree
# Time: O(n), Space: O(n)
# Pseudocode:
#   Serialize: Use preorder traversal, mark null nodes
#   Deserialize: Reconstruct tree from preorder string
class Codec:
    # Time: O(n) | Space: O(n)
    def serialize(self, root):
        def preorder(node):
            if not node:
                vals.append("null")
            else:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        
        vals = []
        preorder(root)
        return ",".join(vals)
    
    # Time: O(n) | Space: O(n)
    def deserialize(self, data):
        def preorder():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node
        
        vals = iter(data.split(","))
        return preorder()

# PROBLEM 9: Validate Binary Search Tree (LC 98)
# Goal: Check if binary tree is valid BST
# Time: O(n), Space: O(h) where h is height of tree
# Pseudocode:
#   1. Use inorder traversal
#   2. Check if values are in ascending order
#   3. Return False if any value is <= previous value
def isValidBST(root):
    def inorder(node):
        if not node:
            return True
        
        if not inorder(node.left):
            return False
        
        if node.val <= self.prev:
            return False
        
        self.prev = node.val
        return inorder(node.right)
    
    self.prev = float('-inf')
    return inorder(root)

# PROBLEM 10: Lowest Common Ancestor (LC 236)
# Goal: Find lowest common ancestor of two nodes in binary tree
# Time: O(n), Space: O(h) where h is height of tree
# Pseudocode:
#   1. If current node is p or q, return current node
#   2. Recursively search left and right subtrees
#   3. If both subtrees return non-null, current node is LCA
#   4. Otherwise, return non-null subtree result
# Time: O(n) | Space: O(h)
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left or right

# PROBLEM 11: Convert Sorted Array to Binary Search Tree (LC 108)
# Goal: Convert sorted array to height-balanced BST
# Time: O(n), Space: O(log n)
# Pseudocode:
#   1. Find middle element as root
#   2. Recursively build left subtree from left half
#   3. Recursively build right subtree from right half
def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root

# PROBLEM 12: Balanced Binary Tree (LC 110)
# Goal: Check if binary tree is height-balanced
# Time: O(n), Space: O(h) where h is height of tree
# Pseudocode:
#   1. For each node, check if left and right subtrees are balanced
#   2. Check if height difference is <= 1
#   3. Return (is_balanced, height) tuple
# Time: O(n) | Space: O(h)
def isBalanced(root):
    def check_balance(node):
        if not node:
            return True, 0
        
        left_balanced, left_height = check_balance(node.left)
        right_balanced, right_height = check_balance(node.right)
        
        is_balanced = (left_balanced and right_balanced and 
                      abs(left_height - right_height) <= 1)
        height = 1 + max(left_height, right_height)
        
        return is_balanced, height
    
    balanced, _ = check_balance(root)
    return balanced

# PROBLEM 13: Binary Tree Right Side View (LC 199)
# Goal: Return values of nodes visible from right side
# Time: O(n), Space: O(w) where w is maximum width of tree
# Pseudocode:
#   1. Use BFS level order traversal
#   2. For each level, take the rightmost node
#   3. Add to result
def rightSideView(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            
            if i == level_size - 1:  # Rightmost node
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# PROBLEM 14: Count Complete Tree Nodes (LC 222)
# Goal: Count nodes in complete binary tree efficiently
# Time: O(log^2 n), Space: O(1)
# Pseudocode:
#   1. Check if left and right subtrees have same height
#   2. If yes, use formula: 2^height - 1
#   3. If no, recursively count left and right subtrees
def countNodes(root):
    if not root:
        return 0
    
    def get_height(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    if left_height == right_height:
        return (2 ** left_height - 1) + 1 + countNodes(root.right)
    else:
        return countNodes(root.left) + 1 + (2 ** right_height - 1)

# PROBLEM 15: Binary Tree Level Order Traversal II (LC 107)
# Goal: Return level order traversal from bottom to top
# Time: O(n), Space: O(w) where w is maximum width of tree
# Pseudocode:
#   1. Use BFS level order traversal
#   2. Reverse the result before returning
def levelOrderBottom(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result[::-1]
