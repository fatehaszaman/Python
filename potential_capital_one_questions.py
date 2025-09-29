# Potential Capital One Questions
# This file contains practice questions that might be asked in Capital One interviews

# =============================================================================
# ARRAY AND STRING PROBLEMS
# =============================================================================

# Question 1: Find the Missing Number
# Given an array of n distinct numbers from 0 to n, identify the missing number.
def find_missing_number(nums):
    # PSEUDOCODE:
    # 1. Calculate what the sum SHOULD be if all numbers 0 to n were present
    # 2. Calculate what the sum ACTUALLY is from the given array
    # 3. The difference is our missing number!
    
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Formula: n*(n+1)/2 for sum of 0 to n
    actual_sum = sum(nums)           # Sum of what we actually have
    return expected_sum - actual_sum # Missing number = expected - actual

# Question 2: Fibonacci Sequence
# Create a function that computes the nth Fibonacci number
def fibonacci(n):
    # PSEUDOCODE:
    # 1. If n is 0 or negative, return 0 (base case)
    # 2. If n is 1, return 1 (base case)
    # 3. Otherwise, add the previous two Fibonacci numbers together
    #    (this is the recursive definition: F(n) = F(n-1) + F(n-2))
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Question 3: Reverse a String
# Develop a function that accepts a string and returns it reversed.
def reverse_string(s):
    # PSEUDOCODE:
    # 1. Use Python's slice notation [::-1] to reverse the string
    #    - [::-1] means: start from end, go to beginning, step by -1
    #    - This is the most Pythonic way to reverse a string!
    
    return s[::-1]

# Question 4: Generate an n x n Star Box
# Given an integer n, return an n x n box made of asterisks (*) for the border, 
# with spaces inside. The box is returned as a list of strings.
def generate_box(n):
    # PSEUDOCODE:
    # 1. If n is less than 1, return empty list (invalid input)
    # 2. For each row from 0 to n-1:
    #    - If it's the first row (i=0) OR last row (i=n-1):
    #      * Make entire row of stars: "****"
    #    - Otherwise (middle rows):
    #      * Make row with star at start, spaces in middle, star at end: "*  *"
    # 3. Add each row to our box list
    # 4. Return the complete box
    
    if n < 1:
        return []
    
    box = []
    for i in range(n):
        if i == 0 or i == n - 1:
            # Top and bottom rows: all stars
            row = '*' * n
        else:
            # Middle rows: star + spaces + star
            row = '*' + ' ' * (n - 2) + '*'
        box.append(row)
    return box

# Question 5: String Array Manipulation
# Given a string array strings (containing only "A" and "P"), and an integer replaceRate.
# Repeatedly apply rules until unable to continue:
# - If consecutive "P"s at end >= replaceRate: Remove replaceRate "P"s, insert one "A" at start
# - Else if there's at least one "A": Replace the last "A" with a "P"
# - Else: stop
# Calculate the number of rounds needed to complete the process.
def count_rounds(strings, replaceRate):
    # PSEUDOCODE:
    # 1. Convert string array to list so we can modify it
    # 2. Keep looping until we can't continue:
    #    - If no "A" characters left, we're done (break)
    #    - Count how many "P"s are at the end of the array
    #    - If we have enough "P"s at the end (>= replaceRate):
    #      * Remove that many "P"s from the end
    #      * Add one "A" at the beginning
    #    - Otherwise:
    #      * Find the last "A" and change it to "P"
    #    - Count this as one round
    # 3. Return total number of rounds
    
    arr = list(strings)  # Convert to list for modifications
    rounds = 0
    while True:
        # Check if any "A" remains; if not, stop
        if "A" not in arr:
            break
        # Count consecutive "P"s at the end
        p_count = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == "P":
                p_count += 1
            else:
                break
        if p_count >= replaceRate:
            # Remove replaceRate "P"s from the end
            arr = arr[:-replaceRate]
            # Insert "A" at the start
            arr.insert(0, "A")
        else:
            # Find and replace the last "A" with "P"
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] == "A":
                    arr[i] = "P"
                    break
        rounds += 1
    return rounds

# Question 6: Longest Shared Prefix
# Given two integer arrays arr1 and arr2, treat each number as a string and find 
# the longest shared prefix between any pair of elements (one from each array).
def longest_shared_prefix(arr1, arr2):
    # PSEUDOCODE:
    # 1. Convert all numbers in both arrays to strings
    # 2. Keep track of the longest prefix found so far
    # 3. For every pair of strings (one from each array):
    #    - Compare characters from left to right until they don't match
    #    - Take the matching part as the current prefix
    #    - If this prefix is longer than our best, update our best
    # 4. Return the longest prefix found across all pairs
    
    str1 = [str(num) for num in arr1]
    str2 = [str(num) for num in arr2]
    max_prefix = ""
    for s1 in str1:
        for s2 in str2:
            # Compute LCP for current pair
            i = 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i += 1
            current_prefix = s1[:i]
            if len(current_prefix) > len(max_prefix):
                max_prefix = current_prefix
    return max_prefix

# =============================================================================
# CAPITAL ONE SPECIFIC PROBLEMS (From their website)
# =============================================================================

# Question 7: Array Manipulation
# Given an array a, output an array b of the same length by applying:
# b[i] = a[i-1] + a[i] + a[i+1] (use 0 for non-existent elements)
def solution_array_manipulation(a):
    n = len(a)
    b = [0 for _ in range(n)]
    for i in range(n):
        b[i] = a[i]
        if i > 0:
            b[i] += a[i - 1]
        if i < n - 1:
            b[i] += a[i + 1]
    return b

# Question 8: String Pattern Matching
# Given pattern (0s and 1s) and source (lowercase letters), calculate the number 
# of substrings of source that match pattern:
# - 0 in pattern = vowel in substring
# - 1 in pattern = consonant in substring
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def check_for_pattern(pattern, source, start_index):
    for offset in range(len(pattern)):
        if pattern[offset] == '0':
            if source[start_index + offset] not in vowels:
                return 0
        else:
            if source[start_index + offset] in vowels:
                return 0
    return 1

def solution_pattern_matching(pattern, source):
    answer = 0
    for start_index in range(len(source) - len(pattern) + 1):
        answer += check_for_pattern(pattern, source, start_index)
    return answer

# Question 9: Two-Dimensional Array Traversal
# Given a game field matrix and a 3x3 figure matrix, find the dropping position 
# such that at least one full row is formed.
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

# Question 10: Lookup Table
# Given an array of unique integers, find the number of pairs of indices (i, j) 
# such that i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2.
from collections import defaultdict

def solution_lookup_table(numbers):
    counts = defaultdict(int)
    answer = 0
    for element in numbers:
        counts[element] += 1
        for two_power in range(21):
            second_element = (1 << two_power) - element
            answer += counts[second_element]
    return answer

# =============================================================================
# LEETCODE-STYLE PROBLEMS
# =============================================================================

# Question 11: Remove Duplicates from Sorted Array
# Given a sorted array of integers, remove duplicates in-place and return the new length.
def removeDuplicates(nums):
    # PSEUDOCODE (Two Pointer Technique):
    # 1. If array is empty, return 0
    # 2. Use two pointers: 'write' (where to write next unique element) and 'read' (current element)
    # 3. Start with write=1 (first element is always unique)
    # 4. For each element from index 1 onwards:
    #    - If current element is different from the last written element:
    #      * Write current element at 'write' position
    #      * Move 'write' pointer forward
    # 5. Return 'write' as the new length (number of unique elements)
    
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write-1]:
            nums[write] = nums[read]
            write += 1
    return write

# Question 12: Valid Parentheses with Wildcard
# Given a string containing (, ), and * (where * can be (, ), or empty), 
# check if it forms a valid parentheses sequence.
def checkValidString(s):
    # PSEUDOCODE (Range Tracking):
    # 1. Track the range of possible open parentheses: [low, high]
    # 2. For each character:
    #    - If '(': both low and high increase by 1
    #    - If ')': both low and high decrease by 1 (but low can't go below 0)
    #    - If '*': low decreases by 1 (treat as ')'), high increases by 1 (treat as '(')
    # 3. If high ever goes negative, it's impossible to balance (return false)
    # 4. At the end, if low == 0, we can balance the parentheses (return true)
    
    low, high = 0, 0  # Track min/max open parentheses
    for c in s:
        if c == '(':
            low += 1
            high += 1
        elif c == ')':
            low = max(0, low - 1)
            high -= 1
        else:  # c == '*'
            low = max(0, low - 1)  # Treat * as )
            high += 1  # Treat * as (
        if high < 0:  # More ) than possible (
            return False
    return low == 0

# Question 13: Word Break
# Given a string s and a dictionary of words, determine if s can be segmented 
# into a space-separated sequence of dictionary words.
def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if i >= len(word) and dp[i - len(word)]:
                if s[i - len(word):i] == word:
                    dp[i] = True
                    break
    return dp[len(s)]

# Question 14: Reverse Words in a String
# Given a string, reverse the order of words. Words are separated by spaces.
def reverseWords(s):
    words = [word for word in s.split() if word]  # Split and filter empty
    return ' '.join(words[::-1])  # Reverse and join

# Question 15: Two Sum with Indices
# Given a sorted array of integers and a target sum, return the 1-based indices 
# of two numbers that add up to the target.
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Question 16: Longest Valid Parentheses
# Given a string containing only ( and ), find the length of the longest 
# valid parentheses substring.
def longestValidParentheses(s):
    stack = [-1]  # Base index for valid substring
    max_length = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:  # char == ')'
            stack.pop()
            if not stack:  # Reset base
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length

# Question 17: Minimum Window Substring
# Given strings s and t, find the minimum window in s that contains all 
# characters in t (with multiplicity).
from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""
    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    window_counts = {}
    left = right = 0
    min_len = float('inf')
    min_window = ""
    while right < len(s):
        # Add character to window
        window_counts[s[right]] = window_counts.get(s[right], 0) + 1
        if s[right] in t_count and window_counts[s[right]] == t_count[s[right]]:
            formed += 1
        # Shrink window
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]
            window_counts[s[left]] -= 1
            if s[left] in t_count and window_counts[s[left]] < t_count[s[left]]:
                formed -= 1
            left += 1
        right += 1
    return min_window

# Question 18: Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric 
# characters and ignoring cases.
def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Question 19: Group Anagrams
# Given an array of strings, group all anagrams together.
def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        anagrams[tuple(count)].append(s)
    return list(anagrams.values())

# Question 20: Reverse Vowels
# Given a string, reverse the order of vowels while keeping other characters in place.
def reverseVowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)  # Strings are immutable
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

# Question 21: Find All Anagrams in a String
# Given two strings s and p, find all starting indices of p's anagrams in s.
def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])
    result = [0] if window_count == p_count else []
    for i in range(len(p), len(s)):
        window_count[s[i]] = window_count.get(s[i], 0) + 1
        window_count[s[i - len(p)]] -= 1
        if window_count[s[i - len(p)]] == 0:
            del window_count[s[i - len(p)]]
        if window_count == p_count:
            result.append(i - len(p) + 1)
    return result

# Question 22: Longest Palindromic Substring
# Given a string, find the longest substring that is a palindrome.
def longestPalindrome(s):
    n = len(s)
    start = max_len = 0
    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1  # Start, length
    for i in range(n):
        # Odd length
        left, length = expand(i, i)
        if length > max_len:
            start, max_len = left, length
        # Even length
        left, length = expand(i, i + 1)
        if length > max_len:
            start, max_len = left, length
    return s[start:start + max_len]

# Question 23: Longest Substring with At Most K Distinct Characters
# Given a string and an integer k, find the length of the longest substring 
# with at most k distinct characters.
def lengthOfLongestSubstringKDistinct(s, k):
    if k == 0:
        return 0
    char_count = defaultdict(int)
    left = 0
    max_len = 0
    for right in range(len(s)):
        char_count[s[right]] += 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Question 24: Subarray Sum Equals K
# Given an array of integers and a target sum k, return the number of subarrays that sum to k.
def subarraySum(nums, k):
    prefix_sum = 0
    count = 0
    sums = defaultdict(int)
    sums[0] = 1  # Empty subarray for sum = k
    for num in nums:
        prefix_sum += num
        count += sums[prefix_sum - k]
        sums[prefix_sum] += 1
    return count

# Question 25: Remove All Adjacent Duplicates
# Given a string, remove all adjacent duplicate characters repeatedly until no duplicates remain.
def removeDuplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

# Question 26: Longest Substring Without Repeating Characters
# Implement a function to find the longest substring without repeating characters.
def longest_unique_substring(s: str) -> str:
    seen = {}
    start = 0
    max_len = 0
    max_substring = ""
    for i, char in enumerate(s):
        # If char was seen and is inside the current window, move the start
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        window_len = i - start + 1
        
        if window_len > max_len:
            max_len = window_len
            max_substring = s[start:i+1]
    return max_substring

# =============================================================================
# FINANCIAL/BANKING PROBLEMS (Capital One Specific)
# =============================================================================

# Question 27: Validate Credit Card Number
# Implement Luhn algorithm to validate credit card numbers
def validate_credit_card_number(card_number):
    # PSEUDOCODE (Luhn Algorithm):
    # 1. Clean the card number: remove spaces, dashes, dots
    # 2. Check if it's all digits and at least 13 characters long
    # 3. Work backwards through the digits:
    #    - For every 2nd digit (from right): double it
    #    - If doubling gives a 2-digit number: add the digits together
    #    - Add all processed digits together
    # 4. If the total sum is divisible by 10, the card is valid!
    
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

# Question 28: Find Maximum Investment Profit
# Given stock prices, find the maximum profit from buying and selling once
def find_max_investment_profit(stock_prices):
    # PSEUDOCODE (Kadane's Algorithm for Stock Problem):
    # 1. If array is empty or has less than 2 prices, return 0 (can't buy and sell)
    # 2. Keep track of the minimum price seen so far
    # 3. Keep track of the maximum profit seen so far
    # 4. For each price:
    #    - If current price is lower than our minimum, update minimum
    #    - Calculate profit if we sold at current price (current - minimum)
    #    - If this profit is better than our best, update best profit
    # 5. Return the maximum profit found
    
    # IF array empty OR length < 2 THEN return 0
    if not stock_prices or len(stock_prices) < 2:
        return 0
    # minimum = prices[0]
    min_cost = stock_prices[0]
    max_profit = 0
    # For each price: if < min, update min
    # profit = current - min 
    for current_price in stock_prices:
        if current_price < min_cost:
            min_cost = current_price
        # if profit > best, update best
        profit = current_price - min_cost
        if profit > max_profit:
            max_profit = profit
    return max_profit

# Question 29: Bank Account Operations
# Process transfer operations between bank accounts
def bank_account_operations(initial_accounts, transfer_operations):
    # PSEUDOCODE:
    # 1. Make a copy of the initial account balances
    # 2. Keep track of successful and failed operations
    # 3. For each transfer operation:
    #    - Parse the operation: "from_account|to_account|amount"
    #    - Check if the source account has enough money
    #    - If yes: subtract from source, add to destination, mark as success
    #    - If no: mark as failed due to insufficient funds
    #    - If parsing fails: mark as failed due to bad format
    # 4. Return final account balances and success count
    
    # copy initial account dict
    accounts = initial_accounts.copy()
    successful = []
    failed = []
    # For each transfer: check funds first 
    # IF enough: subtract from source, add to dest
    # ELSE: add to failed list
    for operation in transfer_operations:
        try:
            from_account, to_account, amount = operation.split('|')
            amount = float(amount)
           
            if accounts.get(from_account, 0) >= amount:
                # subtract FROM destination FIRST
                # if enough: subtract from source, add to dest
                # 4. ELSE: add to failed list
                accounts[from_account] -= amount
                accounts[to_account] = accounts.get(to_account, 0) + amount
                successful.append('Success')
            else:
                failed.append('No money')
        except:
            failed.append('Bad format') 
    # Return final balances + results
    return {'accounts': accounts, 'success_count': len(successful)}

# Question 30: Analyze Transactions
# Calculate balance from transaction strings with + and - operations
def analyze_transactions(transactions):
    # PSEUDOCODE:
    # 1. Start with balance = 0
    # 2. For each transaction string:
    #    - Remove any extra whitespace
    #    - If the string contains "+": add the number to balance
    #    - If the string contains "-": subtract the number from balance
    # 3. Return the final balance
    
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

# Question 31: Matrix Elements Sum
# After removing rows and columns with 0s, sum remaining elements
def matrixElementsSum(matrix):
    # PSEUDOCODE:
    # 1. If matrix is empty, return 0
    # 2. Go through each column from left to right
    # 3. For each column, go down from top to bottom
    # 4. If we find a 0 in a column, STOP counting that column
    #    (because 0s "block" everything below them)
    # 5. Add up all the numbers we can still count
    # 6. Return the total sum
    
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    total = 0
    
    for col in range(cols):
        for row in range(rows):
            if matrix[row][col] == 0:
                break  # Stop counting below this row
            total += matrix[row][col]
    
    return total

# Question 32: All Longest Strings
# Return array of all longest strings from input array
def allLongestStrings(inputArray):
    # PSEUDOCODE:
    # 1. If array is empty, return empty array
    # 2. Find the length of the longest string in the array
    # 3. Go through the array again and collect all strings that have that length
    # 4. Return the collection of longest strings
    
    if not inputArray:
        return []
    
    max_len = max(len(s) for s in inputArray)
    return [s for s in inputArray if len(s) == max_len]

# Question 33: Common Character Count
# Count common characters between two strings (case sensitive)
def commonCharacterCount(s1, s2):
    # PSEUDOCODE:
    # 1. Count how many times each character appears in string 1
    # 2. Count how many times each character appears in string 2
    # 3. For each character that appears in BOTH strings:
    #    - Take the smaller count (we can only use as many as the string with fewer)
    #    - Add that to our total count
    # 4. Return the total number of common characters
    
    from collections import Counter
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    total = 0
    for char in count1:
        if char in count2:
            total += min(count1[char], count2[char])
    
    return total

# Question 34: Is Lucky
# Check if sum of first half equals sum of second half of digits
def isLucky(n):
    # PSEUDOCODE:
    # 1. Convert number to string so we can work with individual digits
    # 2. If the number has odd number of digits, it can't be "lucky" (return false)
    # 3. Split the string into two equal halves
    # 4. Add up all digits in the first half
    # 5. Add up all digits in the second half
    # 6. Return true if both sums are equal, false otherwise
    
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = sum(int(d) for d in s[:mid])
    second_half = sum(int(d) for d in s[mid:])
    
    return first_half == second_half

# Question 35: Sort by Height
# Sort people by height, keeping trees (-1) in place
def sortByHeight(a):
    # PSEUDOCODE:
    # 1. Extract all the people (non-tree values) from the array
    # 2. Sort the people by height (ascending order)
    # 3. Go through the original array and rebuild it:
    #    - If we see a tree (-1), keep it in the same position
    #    - If we see a person, replace it with the next person from our sorted list
    # 4. Return the new array with people sorted but trees in original positions
    
    people = [h for h in a if h != -1]
    people.sort()
    
    result = []
    people_idx = 0
    
    for h in a:
        if h == -1:
            result.append(-1)
        else:
            result.append(people[people_idx])
            people_idx += 1
    
    return result

# Question 36: Reverse Parentheses
# Reverse characters inside each pair of parentheses
def reverseParentheses(s):
    # PSEUDOCODE:
    # 1. Use a stack to keep track of where each opening parenthesis starts
    # 2. Go through each character in the string:
    #    - If it's an opening '(', remember where we are in the result
    #    - If it's a closing ')', get the start position and reverse everything from there
    #    - If it's a regular character, just add it to our result
    # 3. Return the final string with all parentheses content reversed
    
    stack = []
    result = []
    
    for char in s:
        if char == '(':
            stack.append(len(result))
        elif char == ')':
            start = stack.pop()
            result[start:] = result[start:][::-1]
        else:
            result.append(char)
    
    return ''.join(result)

# Question 37: Alternating Sums
# Split array into two teams, return sums of each team
def alternatingSums(a):
    # PSEUDOCODE:
    # 1. Team 1 gets all elements at even positions (0, 2, 4, 6...)
    # 2. Team 2 gets all elements at odd positions (1, 3, 5, 7...)
    # 3. Sum up all elements for each team
    # 4. Return both sums as a list [team1_sum, team2_sum]
    
    team1 = sum(a[i] for i in range(0, len(a), 2))
    team2 = sum(a[i] for i in range(1, len(a), 2))
    return [team1, team2]

# Question 38: Add Border
# Add border of asterisks around picture
def addBorder(picture):
    # PSEUDOCODE:
    # 1. If picture is empty, return empty array
    # 2. Calculate the width of the picture (length of first row)
    # 3. Create a top border: asterisks with width + 2 (for left and right borders)
    # 4. For each row in the picture, add asterisks on left and right sides
    # 5. Add a bottom border (same as top border)
    # 6. Return the picture with borders added
    
    if not picture:
        return []
    
    width = len(picture[0])
    border = '*' * (width + 2)
    
    result = [border]
    for row in picture:
        result.append('*' + row + '*')
    result.append(border)
    
    return result

# Question 39: Are Similar
# Check if two arrays are similar (can swap at most one pair)
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

# Question 40: Array Change
# Count minimum moves to make array strictly increasing
def arrayChange(inputArray):
    moves = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            needed = inputArray[i-1] + 1
            moves += needed - inputArray[i]
            inputArray[i] = needed
    return moves

# Question 41: Palindrome Rearranging
# Check if string can be rearranged into palindrome
def palindromeRearranging(inputString):
    from collections import Counter
    char_count = Counter(inputString)
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    return odd_count <= 1

# Question 42: Are Equally Strong
# Check if two people are equally strong (arms and legs)
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    your_strong = max(yourLeft, yourRight)
    your_weak = min(yourLeft, yourRight)
    friend_strong = max(friendsLeft, friendsRight)
    friend_weak = min(friendsLeft, friendsRight)
    
    return your_strong == friend_strong and your_weak == friend_weak

# Question 43: Array Maximal Adjacent Difference
# Find maximal absolute difference between adjacent elements
def arrayMaximalAdjacentDifference(inputArray):
    max_diff = 0
    for i in range(len(inputArray) - 1):
        diff = abs(inputArray[i] - inputArray[i + 1])
        max_diff = max(max_diff, diff)
    return max_diff

# Question 44: Is IPv4 Address
# Check if string is valid IPv4 address
def isIPv4Address(inputString):
    parts = inputString.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if len(part) > 1 and part[0] == '0':  # No leading zeros
            return False
    
    return True

# Question 45: Avoid Obstacles
# Find minimal jump length to avoid all obstacles
def avoidObstacles(inputArray):
    if not inputArray:
        return 1
    
    max_obstacle = max(inputArray)
    
    for jump in range(1, max_obstacle + 2):
        if all(pos % jump != 0 for pos in inputArray):
            return jump
    
    return max_obstacle + 1

# =============================================================================
# TESTING EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test some functions
    print("Testing find_missing_number:", find_missing_number([0, 1, 3, 4]))  # Should return 2
    print("Testing fibonacci:", fibonacci(5))  # Should return 5
    print("Testing reverse_string:", reverse_string("hello"))  # Should return "olleh"
    
    # Test star box
    print("\nTesting generate_box(4):")
    for row in generate_box(4):
        print(row)