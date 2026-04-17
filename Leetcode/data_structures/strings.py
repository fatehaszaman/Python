# String Problems
# Collection of string manipulation problems from LeetCode, CodeSignal, and other platforms

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# STRING PROBLEMS
# =============================================================================

# PROBLEM: Longest Substring Without Repeating Characters (LC 3)
# Goal: Find the length of the longest substring without repeating characters
# This uses the sliding window technique with two pointers
# Pseudocode:
#   1. Use two pointers: left (start of window) and right (end of window)
#   2. Expand right pointer and add characters to set
#   3. If duplicate found, shrink window from left until no duplicates
#   4. Track maximum window size seen
# Time: O(n) | Space: O(min(m,n))
def lengthOfLongestSubstring(s):
   char_set = set()  # Track characters in current window
   left = 0  # Left boundary of sliding window
   max_len = 0  # Maximum substring length found
   for right in range(len(s)):  # Expand right boundary
       while s[right] in char_set:  # If current character is duplicate
           char_set.remove(s[left])  # Remove character at left boundary
           left += 1  # Shrink window from left
       char_set.add(s[right])  # Add current character to set
       max_len = max(max_len, right - left + 1)  # Update maximum length
   return max_len

# PROBLEM: First Unique Character (LC 387)
# Goal: Find the index of the first non-repeating character in a string
# This uses frequency counting to find the first character with count 1
# Pseudocode:
#   1. Count frequency of each character in the string
#   2. Iterate through string to find first character with count 1
#   3. Return index of first unique character, or -1 if none found
def firstUniqChar(s):
   from collections import Counter
   count = Counter(s)  # Count frequency of each character
   for i, char in enumerate(s):  # Iterate through string with indices
       if count[char] == 1:  # If character appears only once
           return i  # Return its index
   return -1  # No unique character found

# PROBLEM: Group Anagrams (LC 49)
# Goal: Group strings that are anagrams of each other
# This uses sorted string as key to group anagrams together
# Pseudocode:
#   1. For each string, sort its characters to create a key
#   2. Group strings with the same key together
#   3. Return all groups as a list of lists
# Time: O(n*k*log(k)) | Space: O(n*k)
def groupAnagrams(strs):
   from collections import defaultdict
   anagram_map = defaultdict(list)  # Map sorted string -> list of anagrams
   for s in strs:  # Process each string
       # Sort characters to get key (anagrams will have same sorted key)
       key = ''.join(sorted(s))
       anagram_map[key].append(s)  # Add string to its group
   return list(anagram_map.values())  # Return all groups

# PROBLEM: Valid Anagram (LC 242)
# Goal: Check if two strings are anagrams (same characters, different order)
# This uses character counting with a single array
# Pseudocode:
#   1. If lengths differ, not anagrams
#   2. Use array to count characters: +1 for s, -1 for t
#   3. If all counts are 0, strings are anagrams
# Time: O(n log n) | Space: O(1)
def isAnagram(s, t):
   if len(s) != len(t):  # Different lengths can't be anagrams
       return False
   char_count = [0] * 26  # Count for each letter (a-z)
   for i in range(len(s)):  # Process each character
       char_count[ord(s[i]) - ord('a')] += 1  # Increment count for s
       char_count[ord(t[i]) - ord('a')] -= 1  # Decrement count for t
   return all(count == 0 for count in char_count)  # All counts should be 0

# PROBLEM: Longest Common Prefix (LC 14)
# Goal: Find the longest common prefix among all strings in array
# This uses vertical scanning - compare characters at same position
# Pseudocode:
#   1. Start with first string as initial prefix
#   2. For each remaining string, shorten prefix until it matches
#   3. If prefix becomes empty, no common prefix exists
#   4. Return final common prefix
# Time: O(n*m) | Space: O(1)
def longestCommonPrefix(strs):
   if not strs:  # Edge case: empty array
       return ""
   prefix = strs[0]  # Start with first string as prefix
   for string in strs[1:]:  # Compare with each remaining string
       while not string.startswith(prefix):  # While prefix doesn't match
           prefix = prefix[:-1]  # Remove last character
           if not prefix:  # If prefix becomes empty
               return ""  # No common prefix
   return prefix

# PROBLEM: Roman to Integer (LC 13)
# Goal: Convert Roman numeral string to integer
# This processes characters from right to left, subtracting when smaller value precedes larger
# Pseudocode:
#   1. Create mapping of Roman characters to values
#   2. Process string from right to left
#   3. If current value < previous value, subtract; otherwise add
#   4. Return total sum
# Time: O(n) | Space: O(1)
def romanToInt(s):
   roman_values = {  # Mapping of Roman characters to values
       'I': 1, 'V': 5, 'X': 10, 'L': 50,
       'C': 100, 'D': 500, 'M': 1000
   }
   total = 0  # Running total
   prev_value = 0  # Previous character value
   for char in reversed(s):  # Process from right to left
       value = roman_values[char]  # Get current character value
       if value < prev_value:  # If current < previous (subtraction case)
           total -= value  # Subtract current value
       else:  # If current >= previous (addition case)
           total += value  # Add current value
       prev_value = value  # Update previous value
   return total

# PROBLEM: Implement strStr() (LC 28)
# Goal: Find the index of the first occurrence of needle in haystack
# This uses brute force string matching (can be optimized with KMP algorithm)
# Pseudocode:
#   1. If needle is empty, return 0
#   2. For each possible starting position in haystack
#   3. Check if substring matches needle
#   4. Return first match index, or -1 if not found
# Time: O(n*m) | Space: O(1)
def strStr(haystack, needle):
   if not needle:  # Edge case: empty needle
       return 0
   needle_len = len(needle)  # Length of needle
   for i in range(len(haystack) - needle_len + 1):  # Try each starting position
       if haystack[i:i + needle_len] == needle:  # If substring matches needle
           return i  # Return starting index
   return -1  # Needle not found

# PROBLEM: Count and Say (LC 38)
# Goal: Generate nth term of count-and-say sequence
# This uses recursion to build each term from previous term
# Pseudocode:
#   1. Base case: n=1 returns "1"
#   2. Recursively get (n-1)th term
#   3. Count consecutive digits in previous term
#   4. Build string with "count + digit" for each group
# Time: O(n * 2^n) | Space: O(2^n)
def countAndSay(n):
   if n == 1:
       return "1"
   prev = countAndSay(n - 1)
   result = ""
   count = 1
   for i in range(1, len(prev)):
       if prev[i] == prev[i - 1]:
           count += 1
       else:
           result += str(count) + prev[i - 1]
           count = 1
   result += str(count) + prev[-1]
   return result

# PROBLEM: License Key Formatting (LC 482)
# Goal: Format license key with dashes every k characters
# This processes string from right to left to handle edge cases
# Pseudocode:
#   1. Remove existing dashes and convert to uppercase
#   2. Process characters from right to left
#   3. Add dash every k characters (except at the beginning)
#   4. Return reversed result
def licenseKeyFormatting(s, k):
   cleaned = s.replace('-', '').upper()  # Remove dashes and convert to uppercase
   n = len(cleaned)  # Length of cleaned string
   if n == 0:  # Edge case: empty string
       return ""
   result = []  # Store formatted characters
   for i in range(n - 1, -1, -1):  # Process from right to left
       result.append(cleaned[i])  # Add current character
       if (n - i) % k == 0 and i > 0:  # If k characters processed and not at start
           result.append('-')  # Add dash
   return ''.join(reversed(result))  # Return reversed result

# PROBLEM: Remove Vowels from a String (LC 1119)
# Goal: Remove all vowels from the string
# This filters out vowels using set lookup and list comprehension
# Pseudocode:
#   1. Define set of vowels (both uppercase and lowercase)
#   2. Filter out characters that are vowels
#   3. Join remaining characters into string
def removeVowels(s):
   vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels
   return ''.join(char for char in s if char.lower() not in vowels)  # Filter out vowels

# PROBLEM: Longest Valid Parentheses (LC 32)
# Goal: Find length of longest valid parentheses substring
# This uses stack to track valid parentheses boundaries
# Pseudocode:
#   1. Use stack to track indices of unmatched opening parentheses
#   2. When closing parenthesis found, pop stack and calculate length
#   3. If stack becomes empty, use current index as new starting point
#   4. Track maximum valid length
def longestValidParentheses(s):
    if not s:
        return 0
    stack = [-1]  # Initialize with -1 to handle edge cases
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# PROBLEM: Valid Palindrome (LC 125)
# Goal: Check if string is palindrome considering only alphanumeric characters
# This uses two pointers to compare characters from both ends
# Pseudocode:
#   1. Use two pointers from start and end
#   2. Skip non-alphanumeric characters
#   3. Compare characters (case insensitive)
#   4. Return True if all comparisons match
# Time: O(n) | Space: O(1)
def isPalindrome(s):
   left, right = 0, len(s) - 1  # Initialize pointers
   while left < right:  # Continue while pointers haven't met
       # Skip non-alphanumeric characters
       while left < right and not s[left].isalnum():  # Skip non-alphanumeric from left
           left += 1  # Move left pointer
       while left < right and not s[right].isalnum():  # Skip non-alphanumeric from right
           right -= 1  # Move right pointer
       # Compare characters (case insensitive)
       if s[left].lower() != s[right].lower():  # If characters don't match
           return False  # Not a palindrome
       left += 1  # Move left pointer right
       right -= 1  # Move right pointer left
   return True  # All comparisons matched

# PROBLEM: Integer to Roman (LC 12)
# Goal: Convert integer to Roman numeral
# Pseudocode:
#   1. Create mapping of values to Roman symbols (largest to smallest)
#   2. For each value-symbol pair
#   3. While num >= value, append symbol and subtract value
#   4. Return resulting Roman numeral string
# Time: O(1) | Space: O(1)
def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]
    return result

# PROBLEM: Reverse Integer (LC 7)
# Goal: Reverse the digits of an integer, handling overflow and negative numbers
# This tests your understanding of integer manipulation and overflow handling
# Pseudocode:
#   1. Remember the sign (positive or negative)
#   2. Work with absolute value to make it easier
#   3. Extract digits one by one from right to left
#   4. Build the reversed number digit by digit
#   5. Apply the original sign
#   6. Check for 32-bit integer overflow
def reverse(x):
    sign = -1 if x < 0 else 1  # Remember if original number was negative
    x = abs(x)  # Work with positive number to make it easier
    result = 0  # Build the reversed number here
    while x > 0:  # While there are digits left
        result = result * 10 + x % 10  # Add the last digit of x to result
        x //= 10  # Remove the last digit from x
    result *= sign  # Apply the original sign
    return result if -2**31 <= result <= 2**31 - 1 else 0  # Check for overflow

# PROBLEM: Valid Anagram (LC 242)
# Goal: Check if two strings are anagrams (same characters, different order)
# This is a classic character counting problem with a clever optimization!
# Pseudocode:
#   1. If lengths are different, they can't be anagrams
#   2. Use a count array for 26 lowercase letters
#   3. For each character in first string: increment count
#   4. For each character in second string: decrement count
#   5. If all counts are zero, they're anagrams!
# Time: O(n), Space: O(1) - limited charset
def isAnagram(s, t):
    if len(s) != len(t):  # Different lengths can't be anagrams
        return False
    count = [0] * 26  # Count array for a-z
    for i in range(len(s)):  # Go through both strings
        count[ord(s[i]) - ord('a')] += 1  # Increment for first string
        count[ord(t[i]) - ord('a')] -= 1  # Decrement for second string
    return all(c == 0 for c in count)  # All counts should be zero

# PROBLEM 1: Valid Parentheses (LC 20)
# Goal: Check if parentheses are valid using stack
# Time: O(n), Space: O(n)
# Pseudocode:
#   1. Use stack to track opening brackets
#   2. For closing bracket, check if matches top of stack
#   3. If valid, pop from stack; if invalid, return False
#   4. Return True if stack is empty
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

# PROBLEM 2: Valid Anagram (LC 242)
# Goal: Check if two strings are anagrams
# Time: O(n), Space: O(1) - limited to 26 characters
# Pseudocode:
#   1. If lengths differ, return False
#   2. Count frequency of each character in both strings
#   3. If counts match for all characters, return True
# Time: O(n log n) | Space: O(1)
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    char_count = [0] * 26
    for i in range(len(s)):
        char_count[ord(s[i]) - ord('a')] += 1
        char_count[ord(t[i]) - ord('a')] -= 1
    
    return all(count == 0 for count in char_count)

# PROBLEM 3: Group Anagrams (LC 49)
# Goal: Group strings that are anagrams using sorted string as key
# Time: O(n * m log m), Space: O(n * m)
# Pseudocode:
#   1. For each string, sort characters to get key
#   2. Group strings with same key together
#   3. Return grouped anagrams
# Time: O(n*k*log(k)) | Space: O(n*k)
def groupAnagrams(strs):
    from collections import defaultdict
    anagram_map = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        anagram_map[key].append(s)
    
    return list(anagram_map.values())

# PROBLEM 4: Longest Common Prefix (LC 14)
# Goal: Find longest common prefix among array of strings
# Time: O(n * m), Space: O(1)
# Pseudocode:
#   1. Start with first string as prefix
#   2. For each subsequent string, shorten prefix until it matches
#   3. Return final prefix
# Time: O(n*m) | Space: O(1)
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# PROBLEM 5: Reverse String (LC 344)
# Goal: Reverse string in-place using two pointers
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Use two pointers at start and end
#   2. Swap characters at both pointers
#   3. Move pointers towards center
def reverseString(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# PROBLEM 6: First Unique Character (LC 387)
# Goal: Find first non-repeating character using character frequency counting
# Time: O(n), Space: O(1) - limited to 26 characters
# Pseudocode:
#   1. Count frequency of each character
#   2. Find first character with frequency 1
#   3. Return its index
def firstUniqChar(s):
    from collections import Counter
    count = Counter(s)
    
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    
    return -1

# PROBLEM 7: Valid Palindrome (LC 125)
# Goal: Check if string is palindrome ignoring non-alphanumeric characters
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Use two pointers at start and end
#   2. Skip non-alphanumeric characters
#   3. Compare characters (case insensitive)
#   4. Move pointers towards center
# Time: O(n) | Space: O(1)
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

# PROBLEM 8: Longest Substring Without Repeating Characters (LC 3)
# Goal: Find length of longest substring without repeating characters
# Time: O(n), Space: O(min(m, n)) where m is charset size
# Pseudocode:
#   1. Use sliding window with two pointers
#   2. Expand right pointer and add characters to set
#   3. If duplicate found, shrink window from left
#   4. Track maximum window size
# Time: O(n) | Space: O(min(m,n))
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# PROBLEM 9: Find All Anagrams in String (LC 438)
# Goal: Find all anagrams of pattern in text using sliding window
# Time: O(n), Space: O(1) - limited to 26 characters
# Pseudocode:
#   1. Count frequency of pattern characters
#   2. Use sliding window to count frequency of text characters
#   3. If frequencies match, add start index to result
def findAnagrams(s, p):
    from collections import Counter
    
    if len(p) > len(s):
        return []
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    # Initialize window
    for i in range(len(p)):
        window_count[s[i]] += 1
    
    if window_count == p_count:
        result.append(0)
    
    # Slide window
    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1
        
        # Remove old character
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        
        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

# PROBLEM 10: Roman to Integer (LC 13)
# Goal: Convert Roman numeral to integer
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Create mapping of Roman to integer values
#   2. Process from right to left
#   3. If current value < previous value, subtract; otherwise add
# Time: O(n) | Space: O(1)
def romanToInt(s):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# =============================================================================
# CODESIGNAL STRING PROBLEMS
# =============================================================================

# PROBLEM 11: Check Palindrome (CodeSignal)
# Goal: Determine if a string reads the same forwards and backwards
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Compare the original string with its reverse
#   2. If they're identical, it's a palindrome
def checkPalindrome(inputString):
    return inputString == inputString[::-1]

# PROBLEM 12: Alphabetic Shift (CodeSignal)
# Goal: Shift each character in string by 1 position in alphabet
# Time: O(n), Space: O(n)
# Pseudocode:
#   1. For each character, shift to next character in alphabet
#   2. Handle 'z' -> 'a' wrap-around
#   3. Return new string
def alphabeticShift(inputString):
    result = []
    for char in inputString:
        if char == 'z':
            result.append('a')
        else:
            result.append(chr(ord(char) + 1))
    return ''.join(result)

# PROBLEM 13: Palindrome Rearranging (CodeSignal)
# Goal: Check if string can be rearranged into a palindrome
# Time: O(n), Space: O(1) - limited to 26 characters
# Pseudocode:
#   1. Count frequency of each character
#   2. At most one character can have odd frequency
#   3. Return True if palindrome is possible
def palindromeRearranging(inputString):
    from collections import Counter
    count = Counter(inputString)
    odd_count = sum(1 for freq in count.values() if freq % 2 == 1)
    return odd_count <= 1

# PROBLEM 14: First Not Repeating Character (CodeSignal)
# Goal: Find first character that appears only once
# Time: O(n), Space: O(1) - limited to 26 characters
# Pseudocode:
#   1. Count frequency of each character
#   2. Find first character with frequency 1
#   3. Return that character
def firstNotRepeatingCharacter(s):
    from collections import Counter
    count = Counter(s)
    
    for char in s:
        if count[char] == 1:
            return char
    
    return '_'

# PROBLEM 15: Variable Name (CodeSignal)
# Goal: Check if string is a valid variable name
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. First character must be letter or underscore
#   2. Remaining characters must be letter, digit, or underscore
#   3. Return True if valid variable name
def variableName(name):
    if not name or not (name[0].isalpha() or name[0] == '_'):
        return False
    
    for char in name[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    
    return True
