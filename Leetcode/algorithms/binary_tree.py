
# PROBLEM: __init__ (LEETCODE)
def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ListNode class for linked list problems
class ListNode:
    


# PROBLEM: __init__ (LEETCODE)
def __init__(self, size):
            self.size = size
            self.tree = [0] * (size + 1)  # 1-based indexing
        


# PROBLEM: update (LEETCODE)
def update(self, index, delta):  # Add delta to position index
            while index <= self.size:
                self.tree[index] += delta
                index += index & -index  # Move to parent
        


# PROBLEM: spiralOrder (LEETCODE)
def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        # Traverse right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        # Traverse left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

# =============================================================================

# QUESTION 116: Spiral Numbers
# Goal: Create N×N matrix with numbers 1 to N*N in spiral order
# Pseudocode:
#   1. Create empty N×N matrix
#   2. Use direction vectors for right, down, left, up
#   3. Fill matrix spirally from 1 to N*N
#   4. Change direction when hitting boundary or filled cell



# PROBLEM: preorder (LEETCODE)
def preorder(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        vals = []
        preorder(root)
        return ",".join(vals)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Decodes encoded data to tree
        


# PROBLEM: trap (LEETCODE)
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# =============================================================================

# QUESTION 125: Combinations (LC 77)
# Goal: Generate all combinations of k numbers from 1 to n
# Pseudocode:
#   1. Use backtracking to build combinations
#   2. For each number from start to n, add it to current combination
#   3. Recursively build rest of combination
#   4. When combination reaches size k, add to result
#   5. Return all combinations
def combine(n: int, k: int) -> List[List[int]]:
    result = []
    
    

