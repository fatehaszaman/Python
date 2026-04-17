
# PROBLEM: addBorder (LEETCODE)
# Time: O(n*m) | Space: O(n*m)
def addBorder(picture):
    if not picture:  # Edge case: empty picture
        return []
    width = len(picture[0])  # Get width from first row
    border = '*' * (width + 2)  # Create top/bottom border
    result = [border]  # Start with top border
    for row in picture:  # Add each row with side borders
        result.append('*' + row + '*')  # Add asterisks on left and right
    result.append(border)  # Add bottom border
    return result


# QUESTION 3: Add Two Numbers (Linked Lists)
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



# PROBLEM: is_increasing (LEETCODE)
def is_increasing(arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True
    
    for i in range(len(sequence)):
        new_seq = sequence[:i] + sequence[i+1:]
        if is_increasing(new_seq):
            return True
    return False



# QUESTION 7: Alphabetic Shift
# Goal: Replace each character with next letter in alphabet ('z' becomes 'a')
# Pseudocode:
#   1. For each character in string
#   2. If character is 'z', replace with 'a'
#   3. Otherwise, replace with next letter in alphabet
#   4. Return resulting string



# PROBLEM: can_complete_circuit (LEETCODE)
# Time: O(n) | Space: O(1)
def can_complete_circuit(gas, cost):
    total_tank = current_tank = 0  # Track total and current gas
    start_station = 0  # Track potential starting station
    for i in range(len(gas)):  # Go through each station
        total_tank += gas[i] - cost[i]  # Update total gas balance
        current_tank += gas[i] - cost[i]  # Update current gas balance
        if current_tank < 0:  # If we can't reach next station
            start_station = i + 1  # Try starting from next station
            current_tank = 0  # Reset current tank
    return start_station if total_tank >= 0 else -1  # Return start if possible, else -1



# QUESTION 51: Generate an n x n Star Box
# Goal: Create a hollow square made of asterisks - like drawing a box with stars!
# This is a classic string manipulation problem that tests your ability to handle edge cases
# Pseudocode:
#   1. Handle edge case: if n < 1, return empty list (can't make a box)
#   2. For each row from 0 to n-1:
#      - If it's the first or last row: fill with all asterisks
#      - Otherwise: first and last character are asterisks, middle is spaces
#   3. Return the list of strings representing each row



# PROBLEM: intersection (LEETCODE)
# Time: O(m+n) | Space: O(min(m,n))
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))

# =============================================================================

# QUESTION 57: Is IPv4 Address
# Goal: Check if a string is a valid IPv4 address
# This is a string validation problem that tests your ability to handle edge cases!
# Pseudocode:
#   1. Split string by dots to get 4 parts
#   2. Check if we have exactly 4 parts
#   3. For each part:
#      - Check if it's all digits
#      - Check if it's between 0 and 255
#      - Check if it has no leading zeros
#   4. Return True if all checks pass, False otherwise



# PROBLEM: reverse_string (LEETCODE)
# Time: O(n) | Space: O(n)
def reverse_string(s):
    return s[::-1]  # Slice notation: [start:end:step] with step=-1


# QUESTION 98: Reverse Integer
# Goal: Reverse the digits of an integer, handling overflow and negative numbers
# This tests your understanding of integer manipulation and overflow handling
# Pseudocode:
#   1. Remember the sign (positive or negative)
#   2. Work with absolute value to make it easier
#   3. Extract digits one by one from right to left
#   4. Build the reversed number digit by digit
#   5. Apply the original sign
#   6. Check for 32-bit integer overflow



# PROBLEM: reverse_list (LEETCODE)
# Time: O(n) | Space: O(1)
def reverse_list(head):
    prev = None  # Previous node (will become new head)
    current = head  # Current node being processed
    while current:  # While there are nodes left
        next_temp = current.next  # Save next node
        current.next = prev  # Reverse the pointer
        prev = current  # Move prev forward
        current = next_temp  # Move current forward
    return prev  # Return new head



# QUESTION 100: Reverse Parentheses
# Goal: Reverse substrings within each pair of parentheses
# Pseudocode:
#   1. Use stack to track position of opening parentheses
#   2. Build result character by character
#   3. When '(' found, save current position
#   4. When ')' found, reverse substring from saved position
#   5. Return final string



# PROBLEM: reverseString (LEETCODE)
# Time: O(n) | Space: O(1)
def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# =============================================================================

# QUESTION 102: Reverse Vowels
# Goal: Reverse only the vowels in a string while keeping consonants in place
# This is a clever two-pointer problem with character filtering!
# Pseudocode:
#   1. Convert string to list (strings are immutable)
#   2. Use two pointers: left at start, right at end
#   3. Skip non-vowel characters by moving pointers
#   4. When both pointers are at vowels, swap them
#   5. Move both pointers and repeat
#   6. Convert back to string



# PROBLEM: reverseVowels (LEETCODE)
# Time: O(n) | Space: O(n)
def reverseVowels(s):
    vowels = set('aeiouAEIOU')  # Set of vowels for fast lookup
    s = list(s)  # Convert to list since strings are immutable
    left, right = 0, len(s) - 1  # Start with pointers at both ends
    while left < right:  # While we haven't checked all pairs
        while left < right and s[left] not in vowels:  # Skip non-vowels from left
            left += 1
        while left < right and s[right] not in vowels:  # Skip non-vowels from right
            right -= 1
        s[left], s[right] = s[right], s[left]  # Swap the vowels
        left += 1  # Move left pointer
        right -= 1  # Move right pointer
    return ''.join(s)  # Convert back to string



# QUESTION 103: Reverse Words in a String
# Goal: Reverse the order of words in a string, handling multiple spaces
# This is a simple but important string manipulation problem!
# Pseudocode:
#   1. Split the string into words, filtering out empty strings
#   2. Reverse the list of words
#   3. Join them back with spaces
#   4. This handles multiple spaces and leading/trailing spaces



# PROBLEM: has_cycle (LEETCODE)
# Time: O(n) | Space: O(1)
def has_cycle(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        
        state[node] = 1
        
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        
        state[node] = 2
        return False
    
    for i in range(numCourses):
        if state[i] == 0 and has_cycle(i):
            return False
    
    return True

# QUESTION 149: Serialize and Deserialize Binary Tree - Import: TreeNode
# Goal: Serialize and deserialize binary tree
# Time: O(n), Space: O(n)
# Pseudocode:
#   Serialize: Use preorder traversal, mark null nodes
#   Deserialize: Reconstruct tree from preorder string
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Encodes tree to single string using preorder traversal
        


# PROBLEM: check_for_pattern (LEETCODE)
# Time: O(m) | Space: O(1)
def check_for_pattern(pattern, source, start_index):
    for offset in range(len(pattern)):  # Check each character in pattern
        if pattern[offset] == '0':  # Pattern expects vowel
            if source[start_index + offset] not in vowels:  # If not vowel
                return 0  # No match
        else:  # Pattern expects consonant
            if source[start_index + offset] in vowels:  # If vowel
                return 0  # No match
    return 1  # All characters matched



# PROBLEM: solution_2d_traversal (LEETCODE)
# Time: O(W*H*F^2) | Space: O(1)
def solution_2d_traversal(field, figure):
    height = len(field)
    width = len(field[0])
    figure_size = len(figure)
    for column in range(width - figure_size + 1):
        row = 1
        while row < height - figure_size + 1:
            can_fit = True
            for dx in range(figure_size):
                for dy in range(figure_size):
                    if field[row + dx][column + dy] == 1 and figure[dx][dy] == 1:
                        can_fit = False
            if not can_fit:
                break
            row += 1
        row -= 1
        for dx in range(figure_size):
            row_filled = True
            for column_index in range(width):
                if not (field[row + dx][column_index] == 1 or
                        (column <= column_index < column + figure_size and
                         figure[dx][column_index - column] == 1)):
                    row_filled = False
            if row_filled:
                return column
    return -1


# QUESTION 128: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example: s = "anagram", t = "nagaram" -> True
# Time: O(n log n), Space: O(1)
# =============================================================================



# PROBLEM: valid_parentheses (LEETCODE)
# Time: O(n) | Space: O(n)
def valid_parentheses(s):
    stack = []  # Stack to keep track of opening brackets
    mapping = {')': '(', '}': '{', ']': '['}  # Map closing to opening brackets
    
    for char in s:  # Go through each character
        if char in mapping:  # If it's a closing bracket
            top = stack.pop() if stack else '#'  # Get the top of stack (or dummy if empty)
            if mapping[char] != top:  # If it doesn't match the expected opening bracket
                return False  # Invalid parentheses
        else:  # It's an opening bracket
            stack.append(char)  # Add it to our stack
    return not stack  # Valid if stack is empty (all brackets matched)



# QUESTION 135: Valid Parentheses with Wildcard
# Goal: Check if a string with wildcards can form valid parentheses
# This is a clever range tracking problem - much better than trying all combinations!
# Pseudocode:
#   1. Track the range of possible open parentheses: [low, high]
#   2. For each character:
#      - If '(': both low and high increase by 1
#      - If ')': both low and high decrease by 1 (but low can't go below 0)
#      - If '*': low decreases by 1 (treat as ')'), high increases by 1 (treat as '(')
#   3. If high ever goes negative, it's impossible to balance
#   4. At the end, if low == 0, we can balance the parentheses


