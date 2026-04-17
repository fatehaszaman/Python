# LeetCode + CodeSignal — Arrays Collection
# Complexity annotations added inline per function (see # Time: ... | Space: ... above each def)


# PROBLEM: __init__ (LEETCODE)
def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# =============================================================================
# QUESTIONS ORGANIZED ALPHABETICALLY
# =============================================================================

# QUESTION 1: Add Border
# Goal: Add a border of asterisks around a 2D picture
# This is a fun string manipulation problem that tests your 2D array skills!
# Pseudocode:
#   1. Handle edge case: empty picture
#   2. Calculate the width of the picture (length of first row)
#   3. Create a top border: asterisks with width + 2 (for left and right borders)
#   4. For each row in the picture, add asterisks on left and right sides
#   5. Add a bottom border (same as top border)
#   6. Return the picture with borders added
# Time: O(n*m) | Space: O(n*m)
def addBorder(picture):
    if not picture:
        return []
    width = len(picture[0])
    border = '*' * (width + 2)
    result = [border]
    for row in picture:
        result.append('*' + row + '*')
    result.append(border)
    return result

# QUESTION 2: Add Border (duplicate - same as above)
# Time: O(n*m) | Space: O(n*m)
def addBorder2(picture):
    if not picture:
        return []
    width = len(picture[0])
    border = '*' * (width + 2)
    result = [border]
    for row in picture:
        result.append('*' + row + '*')
    result.append(border)
    return result



# PROBLEM: add_two_numbers (LEETCODE)
# Time: O(max(m,n)) | Space: O(max(m,n))
def add_two_numbers(l1, l2):
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



# QUESTION 4: Adjacent Elements Product
# Goal: Find the pair of adjacent elements with largest product
# Example: For inputArray = [3, 6, -2, -5, 7, 3], the output should be 21
# Pseudocode:
#   1. Initialize max_product to negative infinity
#   2. Iterate through array (stop before last element)
#   3. Calculate product of current and next element
#   4. Update max_product if current product is larger
#   5. Return max_product
# Time: O(n) | Space: O(1)
def adjacentElementsProduct(inputArray):
    max_product = float('-inf')
    for i in range(len(inputArray) - 1):
        product = inputArray[i] * inputArray[i + 1]
        max_product = max(max_product, product)
    return max_product



# PROBLEM: almostIncreasingSequence (LEETCODE)
# Time: O(n) | Space: O(1)
def almostIncreasingSequence(sequence):
    


# PROBLEM: alternatingSums (LEETCODE)
# Time: O(n) | Space: O(1)
def alternatingSums(a):
    team1 = sum(a[i] for i in range(0, len(a), 2))
    team2 = sum(a[i] for i in range(1, len(a), 2))
    return [team1, team2]


# QUESTION 9: Alternative Median of Two Sorted Arrays (Merge Approach)
# Goal: Find median using merge technique (simpler but less efficient)
# This is an alternative approach that's easier to understand!
# Pseudocode:
#   1. Merge the two arrays until we reach the middle elements
#   2. Keep track of previous and current elements
#   3. For even total length, return average of two middle elements
#   4. For odd total length, return the middle element
# Time Complexity: O(m + n), Space Complexity: O(1)
# Time: O(m+n) | Space: O(1)
def findMedianSortedArraysMerge(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)  # Get array lengths
    total = m + n  # Total number of elements
    is_even = total % 2 == 0  # Check if total length is even
    i = j = 0  # Pointers for both arrays
    prev = curr = 0  # Track previous and current elements
    for _ in range(total // 2 + 1):  # Merge until we reach middle
        prev = curr  # Update previous element
        if i < m and (j >= n or nums1[i] <= nums2[j]):  # Choose from nums1
            curr = nums1[i]  # Current element from nums1
            i += 1  # Advance nums1 pointer
        else:  # Choose from nums2
            curr = nums2[j]  # Current element from nums2
            j += 1  # Advance nums2 pointer
    return (prev + curr) / 2 if is_even else curr  # Return median


# QUESTION 10: Analyze Transactions
# Goal: Calculate balance from transaction strings with + and - operations
# Pseudocode:
#   1. Start with balance = 0
#   2. For each transaction string:
#      - Remove any extra whitespace
#      - If the string contains "+": add the number to balance
#      - If the string contains "-": subtract the number from balance
#   3. Return the final balance
# Time: O(n) | Space: O(1)
def analyzeTransactions(transactions):
    balance = 0
    for transaction in transactions:
        transaction = transaction.strip()
        if '+' in transaction:
            amount = int(transaction.replace('+', '').strip())
            balance += amount
        elif '-' in transaction:
            amount = int(transaction.replace('-', '').strip())
            balance -= amount
    return balance



# PROBLEM: analyze_transactions (LEETCODE)
# Time: O(n) | Space: O(1)
def analyze_transactions(transactions):
    balance = 0
    for tx in transactions:
        tx = str(tx).strip()
        if "+" in tx:
            balance += float(tx.replace("+", ""))
        elif "-" in tx:
            balance -= float(tx.replace("-", ""))
    return balance

# =============================================================================
# CODESIGNAL-SPECIFIC PROBLEMS (Capital One Assessment Platform)
# =============================================================================


# QUESTION 11: Are Equally Strong
# Goal: Check if two people have the same total strength (arms + legs)
# This is a simple comparison problem that tests your ability to handle multiple values!
# Pseudocode:
#   1. Find the stronger and weaker arm/leg for each person
#   2. Compare the stronger arms and stronger legs
#   3. Compare the weaker arms and weaker legs
#   4. Return True if both comparisons match, False otherwise



# PROBLEM: areEquallyStrong (LEETCODE)
# Time: O(1) | Space: O(1)
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    your_strong = max(yourLeft, yourRight)  # Your stronger arm/leg
    your_weak = min(yourLeft, yourRight)  # Your weaker arm/leg
    friend_strong = max(friendsLeft, friendsRight)  # Friend's stronger arm/leg
    friend_weak = min(friendsLeft, friendsRight)  # Friend's weaker arm/leg
    return your_strong == friend_strong and your_weak == friend_weak  # Compare both

# Thorough CodeSignal Questions Collection
# Comprehensive problems with detailed solutions for assessment preparation

# =============================================================================
# EASY LEVEL PROBLEMS
# =============================================================================

# =============================================================================

# QUESTION 12: Are Similar
# Goal: Check if two arrays can be made equal by swapping at most one pair of elements
# This is a clever array comparison problem that tests your attention to detail!
# Pseudocode:
#   1. If arrays are already equal, return True
#   2. Find all positions where elements differ
#   3. If more than 2 differences, return False (need more than one swap)
#   4. If exactly 2 differences, check if swapping them makes arrays equal
#   5. Return True if swapping works, False otherwise
# Time: O(n) | Space: O(n)
def areSimilar(a, b):
    if a == b:
        return True
    
    differences = []
    for i in range(len(a)):
        if a[i] != b[i]:
            differences.append(i)
    
    if len(differences) != 2:
        return False
    
    i, j = differences
    return a[i] == b[j] and a[j] == b[i]



# PROBLEM: solution_array_manipulation (LEETCODE)
# Time: O(n) | Space: O(n)
def solution_array_manipulation(a):
    n = len(a)  # Get the length of the input array
    b = [0 for _ in range(n)]  # Create new array, all zeros
    for i in range(n):  # Go through each position
        b[i] = a[i]  # Start with the current element
        if i > 0:  # If we have a left neighbor
            b[i] += a[i - 1]  # Add the left neighbor
        if i < n - 1:  # If we have a right neighbor
            b[i] += a[i + 1]  # Add the right neighbor
    return b


# QUESTION 15: Array Manipulation
# Goal: Create a new array where each element is the sum of itself and its neighbors
# This is a classic sliding window problem that tests array indexing and boundary handling
# Pseudocode:
#   1. Create a new array of the same length, initialized to 0
#   2. For each position i in the original array:
#      - Start with the element at position i
#      - Add the left neighbor (if it exists)
#      - Add the right neighbor (if it exists)
#      - Store the result in the new array
#   3. Return the transformed array
# Time: O(n) | Space: O(n)
def arrayManipulation(a):
    n = len(a)
    result = [0] * n
    for i in range(n):
        result[i] = a[i]  # Start with current element
        if i > 0:  # Add left neighbor if exists
            result[i] += a[i - 1]
        if i < n - 1:  # Add right neighbor if exists
            result[i] += a[i + 1]
    return result



# PROBLEM: arrayPreviousLess (LEETCODE)
# Time: O(n^2) | Space: O(n)
def arrayPreviousLess(items):
    result = []
    for i in range(len(items)):
        found = -1
        for j in range(i-1, -1, -1):
            if items[j] < items[i]:
                found = items[j]
                break
        result.append(found)
    return result


# QUESTION 18: Array Replace
# Goal: Replace all occurrences of specific element with substitution element
# Pseudocode:
#   1. Iterate through array
#   2. If element equals elemToReplace, replace with substitutionElem
#   3. Otherwise keep original element
#   4. Return new array
# Time: O(n) | Space: O(n)
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if x == elemToReplace else x for x in inputArray]



# PROBLEM: get_color (LEETCODE)
# Time: O(1) | Space: O(1)
def get_color(cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1]) - 1
        return (col + row) % 2
    
    return get_color(cell1) == get_color(cell2)


# QUESTION 29: Circle of Numbers
# Goal: Find number diametrically opposite in circle of n numbers
# Pseudocode:
#   1. Add half of circle size to current position
#   2. Use modulo to wrap around circle
#   3. Return opposite number
# Time: O(1) | Space: O(1)
def circleOfNumbers(n, firstNumber):
    return (firstNumber + n // 2) % n



# PROBLEM: depositProfit (LEETCODE)
# Time: O(log(threshold/deposit)) | Space: O(1)
def depositProfit(deposit, rate, threshold):
    years = 0
    balance = deposit
    
    while balance < threshold:
        balance += balance * rate / 100
        years += 1
    
    return years

# ADDITIONAL MISSING FUNCTIONS FROM EXACT CODESIGNAL
# Merge Two Sorted Lists



# PROBLEM: twoSum (LEETCODE)
# Time: O(n) | Space: O(n)
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Additional Utility Function: Product of Array Except Self
# Goal: Return array where each element is product of all other elements
# Pseudocode:
#   1. Create result array with all 1s
#   2. First pass: calculate left products
#   3. Second pass: calculate right products and multiply
#   4. Return result array



# PROBLEM: productExceptSelf (LEETCODE)
# Time: O(n) | Space: O(1)
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# Additional Utility Function: Binary Search
# Goal: Search for target in sorted array using binary search
# Pseudocode:
#   1. Initialize left and right pointers
#   2. While left <= right, calculate mid
#   3. If nums[mid] == target, return mid
#   4. If nums[mid] < target, search right half
#   5. Otherwise, search left half
#   6. Return -1 if not found



# PROBLEM: binarySearch (LEETCODE)
# Time: O(log n) | Space: O(1)
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



# QUESTION 36: Different Symbols Naive
# Goal: Find number of different characters in string
# Pseudocode:
#   1. Convert string to set (removes duplicates)
#   2. Return length of set



# PROBLEM: missing_number (LEETCODE)
# Time: O(n) | Space: O(1)
def missing_number(nums):
    n = len(nums)  # Length of array (numbers are 0 to n, so n+1 total numbers)
    expected_sum = n * (n + 1) // 2  # Sum of 0+1+2+...+n = n*(n+1)/2
    actual_sum = sum(nums)  # Sum of the numbers we actually have
    return expected_sum - actual_sum  # The missing number is the difference!



# QUESTION 45: Find Peak Element
# Goal: Find any peak element (greater than neighbors) in an array
# This uses binary search with a clever insight!
# Pseudocode:
#   1. Use binary search to find a peak
#   2. If mid > mid+1, peak is in left half (including mid)
#   3. If mid < mid+1, peak is in right half
#   4. Eventually, left == right will point to a peak
# Time: O(log n), Space: O(1)



# PROBLEM: find_peak_element (LEETCODE)
def find_peak_element(nums):
    left, right = 0, len(nums) - 1  # Initialize binary search
    while left < right:  # While search space is valid
        mid = (left + right) // 2  # Calculate mid point
        if nums[mid] > nums[mid + 1]:  # Descending, peak is left
            right = mid  # Search left (including mid)
        else:  # Ascending, peak is right
            left = mid + 1  # Search right
    return left  # Left == right, found peak


# QUESTION 46: Find Missing Number (LC 268)
# Goal: Find the missing number in array containing n distinct numbers from 0 to n
# Pseudocode:
#   1. Expected sum = n * (n + 1) / 2
#   2. Actual sum = sum of array elements
#   3. Missing number = expected sum - actual sum
#   4. Return missing number
# Time: O(n) | Space: O(1)
def findMissingNumber(nums: List[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# QUESTION 47: First Duplicate
# Goal: Find first number that appears twice in array
# Pseudocode:
#   1. Use set to track seen numbers
#   2. For each number, check if already in set
#   3. If yes, return it (first duplicate)
#   4. Otherwise, add to set
#   5. If no duplicate, return -1



# PROBLEM: isHappy (LEETCODE)
# Time: O(log n) | Space: O(1)
def isHappy(n):
    


# PROBLEM: get_next (LEETCODE)
# Time: O(log n) | Space: O(1)
def get_next(n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

# =====================================================================



# QUESTION 55: Integer to Roman (LC 12)
# Goal: Convert integer to Roman numeral
# Pseudocode:
#   1. Create mapping of values to Roman symbols (largest to smallest)
#   2. For each value-symbol pair
#   3. While num >= value, append symbol and subtract value
#   4. Return resulting Roman numeral string
# Time: O(1) | Space: O(1)
def intToRoman(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]
    return result


# QUESTION 56: Intersection of Two Arrays
# Goal: Return array of unique elements common to both arrays
# Example: nums1 = [1,2,2,1], nums2 = [2,2] -> [2]
# Time: O(n + m), Space: O(min(n, m))
# Pseudocode:
#   1. Convert both arrays to sets
#   2. Find intersection of sets
#   3. Convert result back to list



# PROBLEM: find_kth_largest (LEETCODE)
# Time: O(n log k) | Space: O(k)
def find_kth_largest(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]  # Get k largest, return kth


# =============================================================================
# PART 3: ADVANCED CODESIGNAL PROBLEMS (from advanced_codesignal_problems.py)
# =============================================================================


# QUESTION 60: Linked List Cycle
# Goal: Detect if a linked list has a cycle
# This uses Floyd's Tortoise and Hare algorithm - brilliant!
# Pseudocode:
#   1. Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
#   2. If there's a cycle, fast will eventually meet slow
#   3. If fast reaches null, there's no cycle
#   4. This is like two runners on a circular track!
# Time: O(n), Space: O(1)



# PROBLEM: maxSubArray (LEETCODE)
def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

# =============================================================================

# QUESTION 75: Median of Two Sorted Arrays (Hard)
# Goal: Find median of two sorted arrays in O(log(min(m,n))) time
# This is one of the HARDEST problems in coding interviews - master this and you're golden!
# Pseudocode:
#   1. Make sure first array is smaller (for efficiency)
#   2. Use binary search on the smaller array to find partition point
#   3. Calculate corresponding partition in larger array
#   4. Check if partition is correct (left elements <= right elements)
#   5. If correct: return median based on total length
#   6. If not: adjust binary search range
# Time Complexity: O(log(min(m,n))), Space Complexity: O(1)
# Time: O(log(min(m,n))) | Space: O(1)
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # Ensure nums1 is the smaller array (for efficiency)
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)  # Get lengths
    left, right = 0, m  # Binary search on smaller array
    while left <= right:  # Binary search loop
        partition_x = (left + right) // 2  # Partition point in smaller array
        partition_y = (m + n + 1) // 2 - partition_x  # Corresponding partition in larger array
        # Handle edge cases for partition boundaries
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        if max_left_x <= min_right_y and max_left_y <= min_right_x:  # Found correct partition
            if (m + n) % 2 == 0:  # Even total length
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:  # Odd total length
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:  # Too far right in smaller array
            right = partition_x - 1
        else:  # Too far left in smaller array
            left = partition_x + 1
    raise ValueError("Input arrays are not sorted")



# QUESTION 76: Meeting Rooms
# Goal: Determine if a person can attend all meetings (no overlaps)
# This is a simple interval conflict detection problem!
# Pseudocode:
#   1. Sort meetings by start time
#   2. For each meeting, check if it starts before previous meeting ends
#   3. If any overlap is found, return False
#   4. If no overlaps, return True
# Time: O(n log n), Space: O(1)



# PROBLEM: can_attend_meetings (LEETCODE)
def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    for i in range(1, len(intervals)):  # Check each adjacent pair
        if intervals[i][0] < intervals[i-1][1]:  # If current starts before previous ends
            return False  # Overlap detected
    return True  # No overlaps



# QUESTION 77: Merge Intervals
# Goal: Merge all overlapping intervals
# This is a classic interval problem using sorting!
# Pseudocode:
#   1. Sort intervals by start time
#   2. Initialize result with first interval
#   3. For each interval, check if it overlaps with last merged interval
#   4. If overlap: extend the last interval's end
#   5. If no overlap: add as new interval
# Time: O(n log n), Space: O(1)



# PROBLEM: merge_intervals (LEETCODE)
def merge_intervals(intervals):
    if not intervals:  # Edge case: empty list
        return []
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    merged = [intervals[0]]  # Initialize with first interval
    for current in intervals[1:]:  # Go through remaining intervals
        last = merged[-1]  # Get last merged interval
        if current[0] <= last[1]:  # If current overlaps with last
            last[1] = max(last[1], current[1])  # Extend end time
        else:  # No overlap
            merged.append(current)  # Add as new interval
    return merged



# QUESTION 78: Merge Sorted Array
# Goal: Merge two sorted arrays in-place into first array
# Example: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 -> [1,2,2,3,5,6]
# Time: O(m + n), Space: O(1)
# Pseudocode:
#   1. Start from end of both arrays
#   2. Compare elements and place larger one at end of nums1
#   3. Continue until all elements placed
#   4. Copy any remaining elements from nums2



# PROBLEM: merge (LEETCODE)
# Time: O(m+n) | Space: O(1)
def merge(nums1, m, nums2, n):
    # Start from the end
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    # Copy remaining elements from nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# =============================================================================

# QUESTION 79: Merge Two Sorted Lists
# Goal: Merge two sorted linked lists into one sorted list
# This uses the classic merge technique from merge sort!
# Pseudocode:
#   1. Create a dummy node to simplify edge cases
#   2. Compare nodes from both lists
#   3. Attach smaller node to result and advance that list's pointer
#   4. When one list is exhausted, attach remaining list
#   5. Return dummy.next (the actual head of merged list)
# Time: O(n + m), Space: O(1)



# PROBLEM: merge_two_lists (LEETCODE)
def merge_two_lists(l1, l2):
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




# QUESTION 80: Message From Binary Code
# Goal: Decode binary code to string message
# Pseudocode:
#   1. Process binary string in 8-character chunks
#   2. Convert each 8-bit chunk to decimal (ASCII value)
#   3. Convert ASCII value to character
#   4. Concatenate all characters to form message



# PROBLEM: generate (LEETCODE)
# Time: O(n^2) | Space: O(n^2)
def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

# =============================================================================

# QUESTION 89: Plus One
# Goal: Add 1 to large integer represented as array of digits
# Example: digits = [1,2,3] -> [1,2,4]
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Start from rightmost digit
#   2. If digit < 9, increment and return
#   3. If digit = 9, set to 0 and carry over
#   4. If all digits are 9, prepend 1



# PROBLEM: removeDuplicates (LEETCODE)
# Time: O(n) | Space: O(1)
def removeDuplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index

# =============================================================================

# QUESTION 97: Reverse a String using a built-in function
# Goal: Reverse a string using Python's built-in features
# This is the most Pythonic way to reverse a string!
# Pseudocode:
#   1. Use Python's slice notation [::-1] to reverse the string
#   2. [::-1] means: start from end, go to beginning, step by -1
#   3. This is much more efficient than manual character swapping
#   4. One line solution - Python makes it easy!



# PROBLEM: reverse_integer (LEETCODE)
# Time: O(log n) | Space: O(1)
def reverse_integer(x):
    sign = -1 if x < 0 else 1  # Remember if original number was negative
    x = abs(x)  # Work with positive number to make it easier
    result = 0  # Build the reversed number here
    while x > 0:  # While there are digits left
        result = result * 10 + x % 10  # Add the last digit of x to result
        x //= 10  # Remove the last digit from x
    result *= sign  # Apply the original sign
    return result if -2**31 <= result <= 2**31 - 1 else 0  # Check for overflow



# QUESTION 99: Reverse Linked List
# Goal: Reverse a singly linked list iteratively
# This is a classic iterative reversal using three pointers!
# Pseudocode:
#   1. Use three pointers: prev, current, next
#   2. For each node, reverse its next pointer
#   3. Move all pointers one step forward
#   4. Continue until we reach the end
#   5. Return prev (new head)
# Time: O(n), Space: O(1)



# PROBLEM: reverseParentheses (LEETCODE)
def reverseParentheses(s):
    stack = []
    res = []
    for ch in s:
        if ch == '(':
            stack.append(len(res))
        elif ch == ')':
            start = stack.pop()
            res[start:] = res[start:][::-1]
        else:
            res.append(ch)
    return ''.join(res)



# QUESTION 101: Reverse String Manually 
# Goal: Reverse character array in-place using two pointers
# Example: s = ["h","e","l","l","o"] -> ["o","l","l","e","h"]
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Use two pointers: left at start, right at end
#   2. Swap characters at left and right
#   3. Move pointers towards center
#   4. Continue until pointers meet



# PROBLEM: reverseWords (LEETCODE)
# Time: O(n) | Space: O(n)
def reverseWords(s):
    words = [word for word in s.split() if word]  # Split and filter empty strings
    return ' '.join(words[::-1])  # Reverse and join with spaces



# QUESTION 104: Rotate Array
# Goal: Rotate an array to the right by k steps
# This tests your understanding of array slicing and modular arithmetic
# Pseudocode:
#   1. Handle the case where k is larger than array length (use modulo)
#   2. Split array into two parts: last k elements and first n-k elements
#   3. Concatenate them in reverse order
# Time: O(n), Space: O(1)



# PROBLEM: search_rotated (LEETCODE)
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1  # Initialize pointers
    while left <= right:  # Binary search loop
        mid = (left + right) // 2  # Calculate mid point
        if nums[mid] == target:  # Found target
            return mid
        # Determine which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:  # Target in sorted left half
                right = mid - 1  # Search left
            else:  # Target in right half
                left = mid + 1  # Search right
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:  # Target in sorted right half
                left = mid + 1  # Search right
            else:  # Target in left half
                right = mid - 1  # Search left
    return -1  # Target not found



# QUESTION 109: Shape Area
# Goal: Calculate area of n-interesting polygon
# Pseudocode:
#   1. Formula: n*n + (n-1)*(n-1)
#   2. This creates a diamond-like shape
#   3. Return calculated area



# PROBLEM: maxSlidingWindow (LEETCODE)
# Time: O(n) | Space: O(k)
def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []
    # Deque to store indices of elements in decreasing order
    from collections import deque
    dq = deque()
    result = []
    for i in range(len(nums)):
        # Remove elements outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Remove elements smaller than current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        # Add to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# =============================================================================

# QUESTION 113: Sliding Window Median (Hard)
# Goal: Find median of each sliding window of size k
# This is a challenging problem that requires efficient median finding!
# Pseudocode:
#   1. For each window, sort the elements
#   2. Find median based on window size (odd or even)
#   3. Move window by removing leftmost element and adding rightmost
#   4. Note: This is a simple but not optimal approach
#   5. Optimal would use two heaps or balanced BST
# Time Complexity: O(n log k), Space Complexity: O(k)
# Time: O(n*k log k) | Space: O(k)
def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    if not nums or k == 0:  # Edge cases: empty array or window size 0
        return []
    


# PROBLEM: get_median (LEETCODE)
# Time: O(k log k) | Space: O(k)
def get_median(window):  # Helper function to find median
        sorted_window = sorted(window)  # Sort window elements
        mid = k // 2  # Middle index
        if k % 2 == 1:  # Odd window size
            return float(sorted_window[mid])  # Return middle element
        else:  # Even window size
            return (sorted_window[mid-1] + sorted_window[mid]) / 2.0  # Average of two middle elements
    result = []  # Store medians
    window = list(nums[:k])  # Initialize first window
    result.append(get_median(window))  # Add first median
    for i in range(k, len(nums)):  # Slide window
        window.remove(nums[i-k])  # Remove leftmost element
        window.append(nums[i])  # Add rightmost element
        result.append(get_median(window))  # Add median of current window
    return result




# QUESTION 114: Sort by Height
# Goal: Sort people by height while keeping trees (-1) in their original positions
# This is a clever array manipulation problem that tests your ability to handle mixed data!
# Pseudocode:
#   1. Extract all people (non-tree values) from the array
#   2. Sort the people by height in ascending order
#   3. Go through the original array and rebuild it:
#      - If we see a tree (-1), keep it in the same position
#      - If we see a person, replace it with the next person from our sorted list
#   4. Return the new array with people sorted but trees in original positions



# PROBLEM: sortByHeight (LEETCODE)
# Time: O(n log n) | Space: O(n)
def sortByHeight(a):
    people = [h for h in a if h != -1]  # Extract all people (non-tree values)
    people.sort()  # Sort people by height
    result = []  # Build the result array
    people_idx = 0  # Index for the sorted people list
    for h in a:  # Go through original array
        if h == -1:  # If it's a tree
            result.append(-1)  # Keep it in the same position
        else:  # If it's a person
            result.append(people[people_idx])  # Replace with next sorted person
            people_idx += 1  # Move to next person
    return result


# QUESTION 115: Spiral Matrix
# Goal: Return matrix elements in spiral order (clockwise from outside to inside)
# Example: matrix = [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]
# Time: O(m * n), Space: O(1) excluding output
# Pseudocode:
#   1. Track four boundaries: top, bottom, left, right
#   2. Traverse right along top, then down along right
#   3. Traverse left along bottom, then up along left
#   4. Shrink boundaries and repeat until done



# PROBLEM: preorder (LEETCODE)
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


# =============================================================================
# MISSING EXACT CODESIGNAL QUESTIONS
# =============================================================================


# QUESTION 117: Sqrt(x)
# Goal: Find the square root of x (integer part only)
# This uses binary search to find the largest integer whose square <= x
# Pseudocode:
#   1. Handle edge cases: x < 2 returns x
#   2. Use binary search between 2 and x/2
#   3. For each mid value, check if mid^2 equals x
#   4. If mid^2 < x, search right half
#   5. If mid^2 > x, search left half
#   6. Return the largest valid square root
# Time: O(log x), Space: O(1)



# PROBLEM: sudoku (LEETCODE)
def sudoku(grid):
    for row in grid:
        numbers = [x for x in row if x != '.']
        if len(numbers) != len(set(numbers)):
            return False
    
    for col in range(9):
        numbers = [grid[row][col] for row in range(9) if grid[row][col] != '.']
        if len(numbers) != len(set(numbers)):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            numbers = []
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if grid[row][col] != '.':
                        numbers.append(grid[row][col])
            if len(numbers) != len(set(numbers)):
                return False
    
    return True



# QUESTION 123: Combination Sum (LC 39)
# Goal: Find all unique combinations that sum to target
# Pseudocode:
#   1. Use backtracking to explore all combinations
#   2. For each number, decide to include it or skip it
#   3. Can reuse same number multiple times
#   4. Prune when sum exceeds target
#   5. Return all valid combinations
# Time: O(n^(t/m)) | Space: O(t/m)
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    
    


# PROBLEM: twoSum (LEETCODE)
# Time: O(n) | Space: O(n)
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1  # Start with pointers at both ends
    while left < right:  # While we haven't checked all pairs
        curr_sum = numbers[left] + numbers[right]  # Calculate current sum
        if curr_sum == target:  # Found the target!
            return [left + 1, right + 1]  # Return 1-based indices
        elif curr_sum < target:  # Sum too small, need larger numbers
            left += 1  # Move left pointer right
        else:  # Sum too large, need smaller numbers
            right -= 1  # Move right pointer left
    return []  # No solution found


# QUESTION 127: Two-Dimensional Array Traversal
# Goal: Find dropping position for figure such that at least one full row is formed
# Pseudocode:
#   1. Try each possible column position
#   2. For each column, find lowest row where figure can fit
#   3. Place figure and check if any row is complete
#   4. Return column position if successful
#   5. Continue until valid position found



# PROBLEM: isAnagram (LEETCODE)
# Time: O(n log n) | Space: O(1)
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
# Alternative O(n) solution:
# 


# PROBLEM: validate_credit_card_number (LEETCODE)
# Time: O(n) | Space: O(1)
def validate_credit_card_number(card_number):
    # remove spaces and dashes from card
    card = card_number.replace(" ", "").replace("-", "").replace(".", "")
    # if card not all digits OR length < 13 THEN return FALSE
    if not card.isdigit() or len(card) < 13:
        return False
    # Reverse string
    total = 0
    for i, letter in enumerate(reversed(card)):
        digit = int(letter)
        # for each character in reverse order:
        # if position is odd: digit ← digit * 2
        # if digit > 9: digit ← digit % 10 + digit / 10
        # total ← total + digit
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit = digit % 10 + digit // 10
        total += digit
    # return (total % 10 == 0)
    return total % 10 == 0



# QUESTION 137: Variable Name
# Goal: Check if string is valid variable name
# Pseudocode:
#   1. Check if name is empty or starts with digit (invalid)
#   2. Check if all characters are alphanumeric or underscore
#   3. Return True if valid, False otherwise


