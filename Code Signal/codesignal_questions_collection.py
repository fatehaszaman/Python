# CodeSignal Questions Collection
# Extracted from: https://github.com/amshrestha2020/CodeSignal/tree/main
# Categories: Challenges, Company Challenges, Core, Graphs, Interview Practice, Intro, Python
# Note: SQL/Database questions excluded as requested

"""
===============================================================================
                                INTRODUCTION PROBLEMS
===============================================================================
"""

# Problem 1: Check Palindrome
"""
Given the string, check if it is a palindrome.

Example:
- For inputString = "aabaa", the output should be solution(inputString) = true;
- For inputString = "abac", the output should be solution(inputString) = false;
- For inputString = "a", the output should be solution(inputString) = true.
"""
def checkPalindrome(inputString):
    return inputString == inputString[::-1]

# Problem 2: Adjacent Elements Product
"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example:
For inputArray = [3, 6, -2, -5, 7, 3], the output should be solution(inputArray) = 21.
7 and 3 produce the largest product.
"""
def adjacentElementsProduct(inputArray):
    max_product = float('-inf')
    for i in range(len(inputArray) - 1):
        product = inputArray[i] * inputArray[i + 1]
        max_product = max(max_product, product)
    return max_product

# Problem 3: Shape Area
"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side.

Example:
For n = 2, the output should be solution(n) = 5;
For n = 3, the output should be solution(n) = 13.
"""
def shapeArea(n):
    return n * n + (n - 1) * (n - 1)

# Problem 4: Make Array Consecutive 2
"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example:
For statues = [6, 2, 3, 8], the output should be solution(statues) = 3.
Ratiorg needs statues of sizes 4, 5 and 7.
"""
def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1

# Problem 5: Almost Increasing Sequence
"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example:
For sequence = [1, 3, 2, 1], the output should be solution(sequence) = false;
For sequence = [1, 3, 2], the output should be solution(sequence) = true.
"""
def almostIncreasingSequence(sequence):
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

"""
===============================================================================
                                CORE PROBLEMS
===============================================================================
"""

# Problem 6: Array Maximal Adjacent Difference
"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example:
For inputArray = [2, 4, 1, 0], the output should be solution(inputArray) = 3.
"""
def arrayMaximalAdjacentDifference(inputArray):
    max_diff = 0
    for i in range(len(inputArray) - 1):
        diff = abs(inputArray[i] - inputArray[i + 1])
        max_diff = max(max_diff, diff)
    return max_diff

# Problem 7: Is IPv4 Address
"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example:
For inputString = "172.16.254.1", the output should be solution(inputString) = true;
For inputString = "172.316.254.1", the output should be solution(inputString) = false.
"""
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
        if len(part) > 1 and part[0] == '0':
            return False
    
    return True

# Problem 8: Avoid Obstacles
"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example:
For inputArray = [5, 3, 6, 7, 9], the output should be solution(inputArray) = 4.
"""
def avoidObstacles(inputArray):
    max_obstacle = max(inputArray)
    for jump in range(1, max_obstacle + 2):
        if all(coord % jump != 0 for coord in inputArray):
            return jump
    return max_obstacle + 1

# Problem 9: Box Blur
"""
Last night you had to study, but decided to party instead. Now there is a black and white photo of you that's about to go viral. You cannot let this ruin your reputation, so you want to apply box blur algorithm to the photo to hide its content.

The algorithm works as follows: each pixel x in the resulting image has a value equal to the average value of the input image pixels' values from the 3 × 3 square with the center at x. All pixels at the edges are cropped.

As pixel's value is an integer, all fractions should be rounded down.

Example:
For image = [[1, 1, 1], 
             [1, 7, 1], 
             [1, 1, 1]], the output should be solution(image) = [[1]].
"""
def boxBlur(image):
    rows, cols = len(image), len(image[0])
    result = []
    
    for i in range(1, rows - 1):
        row = []
        for j in range(1, cols - 1):
            total = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    total += image[i + di][j + dj]
            row.append(total // 9)
        result.append(row)
    
    return result

# Problem 10: Minesweeper
"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines, we want to create a Minesweeper game setup.

Example:
For matrix = [[true, false, false],
              [false, true, false],
              [false, false, false]], the output should be solution(matrix) = [[1, 2, 1],
                                                                                [2, 1, 1],
                                                                                [1, 1, 1]]
"""
def minesweeper(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        result[ni][nj] += 1
    
    return result

"""
===============================================================================
                                GRAPH PROBLEMS
===============================================================================
"""

# Problem 11: Roads Building
"""
Once upon a time, in a kingdom far, far away, there lived a King Byteasar I. As a kind and wise ruler, he did everything in his (unlimited) power to make life of his subjects comfortable and pleasant. One cold evening a messenger arrived at the king's castle with the latest news: all kings in the Kingdoms Union had started enforcing traffic laws! In order to not lose his membership in the Union, King Byteasar had to do the same within his kingdom. But what would the citizens think of it?

The king decided to start introducing the changes with something more or less simple: change all the roads in the kingdom from two-directional to one-directional. He personally prepared the roadRegister of the new roads, and now he needs to make sure that the road system is convenient and there will be no traffic jams, i.e. each city has the same number of incoming and outgoing roads. As the Hand of the King, you're the one who should check it.

Example:
For roadRegister = [[false, true,  true,  false],
                    [true,  false, true,  false],
                    [true,  true,  false, true ],
                    [false, false, true,  false]], the output should be solution(roadRegister) = true.
"""
def roadsBuilding(roadRegister):
    n = len(roadRegister)
    for i in range(n):
        incoming = sum(roadRegister[j][i] for j in range(n))
        outgoing = sum(roadRegister[i][j] for j in range(n))
        if incoming != outgoing:
            return False
    return True

# Problem 12: Efficient Road Network
"""
Once upon a time, in a kingdom far, far away, there lived a King Byteasar II. There was nothing special about him or his kingdom. As a mediocre ruler, he preferred hunting and feasting over doing anything about his kingdom's prosperity.

Luckily, his adviser, the wise magician Bitlin, worked for the kingdom's welfare day and night. However, since there was no one to advise him, he completely forgot about one important thing: the road network! The kingdom has n cities numbered from 0 to n-1, but some pairs of cities are not connected by a direct road, and this must be fixed.

The roads are already built, but Bitlin realized that he has to redirect traffic, so that information could reach any city from any other city. He decided to make each road one-way.

The kingdom has n cities numbered from 0 to n-1. You are given a list of roads, where roads[i] = [a, b] means there is a direct road between cities a and b (and of course between cities b and a).

Your task is to help Bitlin to redirect each road in such a way that the resulting network is efficient. A network is efficient if it is possible to reach any city from any other city by traversing at most 2 roads.

Return true if it is possible to make the network efficient, otherwise return false.

Example:
For n = 4 and roads = [[0, 1], [1, 2], [2, 0]], the output should be solution(n, roads) = true.
"""
def efficientRoadNetwork(n, roads):
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # Check if each pair of cities is within 2 hops
    for i in range(n):
        for j in range(i + 1, n):
            # Check if i and j are connected within 2 hops
            if j not in graph[i]:  # Not direct neighbors
                # Check if they have a common neighbor
                has_common_neighbor = any(k in graph[i] and k in graph[j] for k in range(n))
                if not has_common_neighbor:
                    return False
    
    return True

"""
===============================================================================
                                INTERVIEW PRACTICE PROBLEMS
===============================================================================
"""

# Problem 13: First Duplicate
"""
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example:
For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.
"""
def firstDuplicate(a):
    seen = set()
    for num in a:
        if num in seen:
            return num
        seen.add(num)
    return -1

# Problem 14: First Not Repeating Character
"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example:
For s = "abacabad", the output should be solution(s) = 'c'.
"""
def firstNotRepeatingCharacter(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return '_'

# Problem 15: Rotate Image
"""
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example:
For a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]], the output should be solution(a) = [[7, 4, 1],
                                                         [8, 5, 2],
                                                         [9, 6, 3]]
"""
def rotateImage(a):
    n = len(a)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    
    # Reverse each row
    for i in range(n):
        a[i] = a[i][::-1]
    
    return a

# Problem 16: Sudoku
"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example:
For grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']], the output should be solution(grid) = true.
"""
def sudoku(grid):
    # Check rows
    for row in grid:
        numbers = [x for x in row if x != '.']
        if len(numbers) != len(set(numbers)):
            return False
    
    # Check columns
    for col in range(9):
        numbers = [grid[row][col] for row in range(9) if grid[row][col] != '.']
        if len(numbers) != len(set(numbers)):
            return False
    
    # Check 3x3 subgrids
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

"""
===============================================================================
                                PYTHON SPECIFIC PROBLEMS
===============================================================================
"""

# Problem 17: Different Symbols Naive
"""
Given a string, find the number of different characters in it.

Example:
For s = "cabca", the output should be solution(s) = 3.
There are 3 different characters a, b and c.
"""
def differentSymbolsNaive(s):
    return len(set(s))

# Problem 18: File Naming
"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example:
For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be solution(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
"""
def fileNaming(names):
    used_names = set()
    result = []
    
    for name in names:
        if name not in used_names:
            used_names.add(name)
            result.append(name)
        else:
            k = 1
            new_name = f"{name}({k})"
            while new_name in used_names:
                k += 1
                new_name = f"{name}({k})"
            used_names.add(new_name)
            result.append(new_name)
    
    return result

# Problem 19: Message From Binary Code
"""
You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.

Example:
For code = "010010000110010101101100011011000110111100100001", the output should be solution(code) = "Hello!".
"""
def messageFromBinaryCode(code):
    result = ""
    for i in range(0, len(code), 8):
        byte = code[i:i+8]
        ascii_value = int(byte, 2)
        result += chr(ascii_value)
    return result

# Problem 20: Spiral Numbers
"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example:
For n = 3, the output should be solution(n) = [[1, 2, 3],
                                               [8, 9, 4],
                                               [7, 6, 5]]
"""
def spiralNumbers(n):
    matrix = [[0] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction_index = 0
    row, col = 0, 0
    current = 1
    
    for _ in range(n * n):
        matrix[row][col] = current
        current += 1
        
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        
        if (next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or 
            matrix[next_row][next_col] != 0):
            direction_index = (direction_index + 1) % 4
            next_row = row + directions[direction_index][0]
            next_col = col + directions[direction_index][1]
        
        row, col = next_row, next_col
    
    return matrix

"""
===============================================================================
                                COMPANY CHALLENGES
===============================================================================
"""

# Problem 21: String Pattern Matching (Already exists in your workspace)
# This is the same as the one you already have in string_pattern_matching.py

# Problem 22: Two Dimensional Array Traversal (Already exists in your workspace)
# This is the same as the one you already have in two_dimensional_array_traversal.py

# Problem 23: Array Manipulation (Already exists in your workspace)
# This is the same as the one you already have in array_manipulation.py

# Problem 24: Lookup Table (Already exists in your workspace)
# This is the same as the one you already have in lookup_table.py

# Problem 25: New Prime Number List (Already exists in your workspace)
# This is the same as the one you already have in new_prime_num_list.py

"""
===============================================================================
                                ADDITIONAL CHALLENGES
===============================================================================
"""

# Problem 26: Palindrome Rearranging
"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example:
For inputString = "aabb", the output should be solution(inputString) = true.
We can rearrange "aabb" to make "abba", which is a palindrome.
"""
def palindromeRearranging(inputString):
    from collections import Counter
    count = Counter(inputString)
    odd_count = sum(1 for freq in count.values() if freq % 2 == 1)
    return odd_count <= 1

# Problem 27: Array Replace
"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example:
For inputArray = [1, 2, 1], elemToReplace = 1, substitutionElem = 3, the output should be solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if x == elemToReplace else x for x in inputArray]

# Problem 28: Even Digits Only
"""
Check if all digits of the given integer are even.

Example:
For n = 248622, the output should be solution(n) = true;
For n = 642386, the output should be solution(n) = false.
"""
def evenDigitsOnly(n):
    return all(int(digit) % 2 == 0 for digit in str(n))

# Problem 29: Variable Name
"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example:
For name = "var_1__Int", the output should be solution(name) = true;
For name = "qq-q", the output should be solution(name) = false;
For name = "2w2", the output should be solution(name) = false.
"""
def variableName(name):
    if name[0].isdigit():
        return False
    return all(c.isalnum() or c == '_' for c in name)

# Problem 30: Alphabetic Shift
"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace 'a' with 'b', replace 'b' with 'c', etc (z would be replaced by a).

Example:
For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
"""
def alphabeticShift(inputString):
    result = ""
    for char in inputString:
        if char == 'z':
            result += 'a'
        else:
            result += chr(ord(char) + 1)
    return result

"""
===============================================================================
                                TESTING FUNCTIONS
===============================================================================
"""

def test_all_functions():
    """Test all the functions to ensure they work correctly"""
    
    # Test Introduction Problems
    assert checkPalindrome("aabaa") == True
    assert checkPalindrome("abac") == False
    
    assert adjacentElementsProduct([3, 6, -2, -5, 7, 3]) == 21
    
    assert shapeArea(2) == 5
    assert shapeArea(3) == 13
    
    assert makeArrayConsecutive2([6, 2, 3, 8]) == 3
    
    assert almostIncreasingSequence([1, 3, 2]) == True
    assert almostIncreasingSequence([1, 3, 2, 1]) == False
    
    # Test Core Problems
    assert arrayMaximalAdjacentDifference([2, 4, 1, 0]) == 3
    
    assert isIPv4Address("172.16.254.1") == True
    assert isIPv4Address("172.316.254.1") == False
    
    assert avoidObstacles([5, 3, 6, 7, 9]) == 4
    
    # Test Interview Practice Problems
    assert firstDuplicate([2, 1, 3, 5, 3, 2]) == 3
    
    assert firstNotRepeatingCharacter("abacabad") == 'c'
    assert firstNotRepeatingCharacter("abacabaabacaba") == '_'
    
    # Test Python Specific Problems
    assert differentSymbolsNaive("cabca") == 3
    
    assert fileNaming(["doc", "doc", "image", "doc(1)", "doc"]) == ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]
    
    assert messageFromBinaryCode("010010000110010101101100011011000110111100100001") == "Hello!"
    
    # Test Additional Challenges
    assert palindromeRearranging("aabb") == True
    assert palindromeRearranging("aabbc") == True
    assert palindromeRearranging("aabbccd") == False
    
    assert arrayReplace([1, 2, 1], 1, 3) == [3, 2, 3]
    
    assert evenDigitsOnly(248622) == True
    assert evenDigitsOnly(642386) == False
    
    assert variableName("var_1__Int") == True
    assert variableName("qq-q") == False
    assert variableName("2w2") == False
    
    assert alphabeticShift("crazy") == "dsbaz"
    
    print("All tests passed!")

"""
===============================================================================
                                MORE INTRODUCTION PROBLEMS
===============================================================================
"""

# Problem 31: All Longest Strings
"""
Given an array of strings, return another array containing all of its longest strings.

Example:
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be solution(inputArray) = ["aba", "vcd", "aba"].
"""
def allLongestStrings(inputArray):
    max_length = max(len(s) for s in inputArray)
    return [s for s in inputArray if len(s) == max_length]

# Problem 32: Common Character Count
"""
Given two strings, find the number of common characters between them.

Example:
For s1 = "aabcc" and s2 = "adcaa", the output should be solution(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c".
"""
def commonCharacterCount(s1, s2):
    from collections import Counter
    count1 = Counter(s1)
    count2 = Counter(s2)
    common = 0
    for char in count1:
        if char in count2:
            common += min(count1[char], count2[char])
    return common

# Problem 33: Is Lucky
"""
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Example:
For n = 1230, the output should be solution(n) = true;
For n = 239017, the output should be solution(n) = false.
"""
def isLucky(n):
    s = str(n)
    mid = len(s) // 2
    first_half = sum(int(digit) for digit in s[:mid])
    second_half = sum(int(digit) for digit in s[mid:])
    return first_half == second_half

# Problem 34: Sort by Height
"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

Example:
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""
def sortByHeight(a):
    people = [h for h in a if h != -1]
    people.sort()
    result = []
    people_index = 0
    
    for h in a:
        if h == -1:
            result.append(-1)
        else:
            result.append(people[people_index])
            people_index += 1
    
    return result

# Problem 35: Reverse Parentheses
"""
You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair.

Example:
For s = "a(bc)de", the output should be solution(s) = "acbde".
"""
def reverseParentheses(s):
    stack = []
    result = ""
    
    for char in s:
        if char == '(':
            stack.append(result)
            result = ""
        elif char == ')':
            result = stack.pop() + result[::-1]
        else:
            result += char
    
    return result

# Problem 36: Alternating Sums
"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example:
For a = [50, 60, 60, 45, 70], the output should be solution(a) = [180, 105].
"""
def alternatingSums(a):
    team1 = sum(a[i] for i in range(0, len(a), 2))
    team2 = sum(a[i] for i in range(1, len(a), 2))
    return [team1, team2]

# Problem 37: Add Border
"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example:
For picture = ["abc", "ded"], the output should be solution(picture) = ["*****", "*abc*", "*ded*", "*****"].
"""
def addBorder(picture):
    width = len(picture[0]) + 2
    border = "*" * width
    result = [border]
    
    for row in picture:
        result.append("*" + row + "*")
    
    result.append(border)
    return result

# Problem 38: Array Previous Less
"""
Given an array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i. If no such value can be found, store -1 instead.

Example:
For items = [3, 5, 2, 4, 5], the output should be solution(items) = [-1, 3, -1, 2, 4].
"""
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

# Problem 39: Array Change
"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example:
For inputArray = [1, 1, 1], the output should be solution(inputArray) = 3.
"""
def arrayChange(inputArray):
    moves = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            needed = inputArray[i-1] + 1
            moves += needed - inputArray[i]
            inputArray[i] = needed
    return moves

"""
===============================================================================
                                MORE CORE ALGORITHMS
===============================================================================
"""

# Problem 41: Array Replace
"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example:
For inputArray = [1, 2, 1], elemToReplace = 1, substitutionElem = 3, the output should be solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if x == elemToReplace else x for x in inputArray]

# Problem 42: Even Digits Only
"""
Check if all digits of the given integer are even.

Example:
For n = 248622, the output should be solution(n) = true;
For n = 642386, the output should be solution(n) = false.
"""
def evenDigitsOnly(n):
    return all(int(digit) % 2 == 0 for digit in str(n))

# Problem 43: Variable Name
"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example:
For name = "var_1__Int", the output should be solution(name) = true;
For name = "qq-q", the output should be solution(name) = false;
For name = "2w2", the output should be solution(name) = false.
"""
def variableName(name):
    if not name or name[0].isdigit():
        return False
    return all(c.isalnum() or c == '_' for c in name)

# Problem 44: Chess Board Cell Color
"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example:
For cell1 = "A1" and cell2 = "C3", the output should be solution(cell1, cell2) = true.
"""
def chessBoardCellColor(cell1, cell2):
    def get_color(cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1]) - 1
        return (col + row) % 2
    
    return get_color(cell1) == get_color(cell2)

# Problem 45: Circle of Numbers
"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example:
For n = 10 and firstNumber = 2, the output should be solution(n, firstNumber) = 7.
"""
def circleOfNumbers(n, firstNumber):
    return (firstNumber + n // 2) % n

# Problem 46: Deposit Profit
"""
You have deposited a specific amount of dollars into your bank account. Each year your balance increases at the same growth rate. Find out how long it would take for your balance to pass a specific threshold with the assumption that you don't make any additional deposits.

Example:
For deposit = 100, rate = 20 and threshold = 170, the output should be solution(deposit, rate, threshold) = 3.
"""
def depositProfit(deposit, rate, threshold):
    years = 0
    balance = deposit
    while balance < threshold:
        balance *= (1 + rate / 100)
        years += 1
    return years

# Problem 47: Absolute Values Sum Minimization
"""
Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)

Example:
For a = [2, 4, 7], the output should be solution(a) = 4.
"""
def absoluteValuesSumMinimization(a):
    return a[len(a) // 2] if len(a) % 2 == 1 else a[len(a) // 2 - 1]

# Problem 48: Strings Rearrangement
"""
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by a single character.

Example:
For inputArray = ["aba", "bbb", "bab"], the output should be solution(inputArray) = false.
"""
def stringsRearrangement(inputArray):
    from itertools import permutations
    
    def differ_by_one(s1, s2):
        return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1
    
    for perm in permutations(inputArray):
        if all(differ_by_one(perm[i], perm[i+1]) for i in range(len(perm)-1)):
            return True
    return False

# Problem 49: Extract Each Kth
"""
Given array of integers, remove each kth element from it.

Example:
For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
"""
def extractEachKth(inputArray, k):
    return [inputArray[i] for i in range(len(inputArray)) if (i + 1) % k != 0]

# Problem 50: First Digit
"""
Find the leftmost digit that occurs in a given string.

Example:
For inputString = "var_1__Int", the output should be solution(inputString) = '1'.
"""
def firstDigit(inputString):
    for char in inputString:
        if char.isdigit():
            return char
    return ''

"""
===============================================================================
                                MORE GRAPH THEORY
===============================================================================
"""

# Problem 51: Remove K From List
"""
Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example:
For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be solution(l, k) = [1, 2, 4, 5].
"""
def removeKFromList(l, k):
    # This is a simplified version for arrays
    # In actual implementation, l would be a linked list node
    result = []
    current = l
    while current is not None:
        if current.value != k:
            result.append(current.value)
        current = current.next
    return result

# Problem 52: Is List Palindrome
"""
Given a singly linked list of integers, determine whether or not it's a palindrome.

Example:
For l = [0, 1, 2, 1, 0], the output should be solution(l) = true.
"""
def isListPalindrome(l):
    # Convert linked list to array for simplicity
    values = []
    current = l
    while current is not None:
        values.append(current.value)
        current = current.next
    
    return values == values[::-1]

# Problem 53: Add Two Huge Numbers
"""
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The linked list elements are in reverse order, such that the first element is the least significant digit of the number.

Example:
For a = [9876, 5432, 1999] and b = [1, 8001], the output should be solution(a, b) = [9876, 5434, 0].
"""
def addTwoHugeNumbers(a, b):
    def list_to_number(lst):
        num = 0
        multiplier = 1
        current = lst
        while current:
            num += current.value * multiplier
            multiplier *= 10000
            current = current.next
        return num
    
    def number_to_list(num):
        if num == 0:
            return ListNode(0)
        
        result = None
        while num > 0:
            digit = num % 10000
            new_node = ListNode(digit)
            new_node.next = result
            result = new_node
            num //= 10000
        
        return result
    
    num_a = list_to_number(a)
    num_b = list_to_number(b)
    sum_num = num_a + num_b
    
    return number_to_list(sum_num)

# Problem 54: Merge Two Linked Lists
"""
Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example:
For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be solution(l1, l2) = [1, 2, 3, 4, 5, 6].
"""
def mergeTwoLinkedLists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 or l2
    return dummy.next

# Problem 55: Reverse Nodes in K-Group
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

Example:
For l = [1, 2, 3, 4, 5] and k = 2, the output should be solution(l, k) = [2, 1, 4, 3, 5].
"""
def reverseNodesInKGroups(l, k):
    def reverse_group(head, k):
        prev = None
        current = head
        count = 0
        
        # Check if we have k nodes
        temp = current
        while temp and count < k:
            temp = temp.next
            count += 1
        
        if count == k:
            # Reverse k nodes
            while count > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count -= 1
            
            if current:
                head.next = reverseNodesInKGroups(current, k)
        
        return prev
    
    return reverse_group(l, k)

"""
===============================================================================
                                MORE INTERVIEW PRACTICE
===============================================================================
"""

# Problem 56: Tree Height
"""
Given a binary tree t, determine its height.

Example:
For t = { value: 1, left: { value: 2, left: null, right: null }, right: { value: 3, left: null, right: null } }, the output should be solution(t) = 2.
"""
def treeHeight(t):
    if t is None:
        return -1
    
    left_height = treeHeight(t.left)
    right_height = treeHeight(t.right)
    
    return max(left_height, right_height) + 1

# Problem 57: Has Path With Given Sum
"""
Given a binary tree t and an integer s, determine whether there is a root-to-leaf path such that adding up all the values along the path equals s.

Example:
For t = { value: 4, left: { value: 1, left: { value: -2, left: null, right: { value: 3, left: null, right: null } }, right: null }, right: { value: 3, left: { value: 1, left: null, right: null }, right: { value: 2, left: { value: -2, left: null, right: null }, right: { value: -3, left: null, right: null } } } } and s = 7, the output should be solution(t, s) = true.
"""
def hasPathWithGivenSum(t, s):
    if t is None:
        return s == 0
    
    if t.left is None and t.right is None:
        return s == t.value
    
    remaining_sum = s - t.value
    
    if t.left and hasPathWithGivenSum(t.left, remaining_sum):
        return True
    
    if t.right and hasPathWithGivenSum(t.right, remaining_sum):
        return True
    
    return False

# Problem 58: Find Profitable Projects
"""
You have a list of projects and their associated profits. You need to find the most profitable project within your budget.

Example:
For projects = [[4, 1], [5, 2], [2, 3]] and budget = 4, the output should be solution(projects, budget) = 3.
"""
def findProfitableProjects(projects, budget):
    max_profit = 0
    for cost, profit in projects:
        if cost <= budget:
            max_profit = max(max_profit, profit)
    return max_profit

# Problem 59: Is Subtree
"""
Given two binary trees t1 and t2, check whether t2 is a subtree of t1.

Example:
For t1 = { value: 5, left: { value: 10, left: { value: 4, left: null, right: null }, right: { value: 6, left: null, right: null } }, right: { value: 7, left: null, right: null } } and t2 = { value: 10, left: { value: 4, left: null, right: null }, right: { value: 6, left: null, right: null } }, the output should be solution(t1, t2) = true.
"""
def isSubtree(t1, t2):
    if t2 is None:
        return True
    if t1 is None:
        return False
    
    def is_same_tree(tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        return (tree1.value == tree2.value and 
                is_same_tree(tree1.left, tree2.left) and 
                is_same_tree(tree1.right, tree2.right))
    
    return (is_same_tree(t1, t2) or 
            isSubtree(t1.left, t2) or 
            isSubtree(t1.right, t2))

# Problem 60: Restore Binary Tree
"""
Given the inorder and preorder traversals of a binary tree, restore the original tree.

Example:
For inorder = [4, 2, 1, 5, 3] and preorder = [1, 2, 4, 3, 5], the output should be the restored tree.
"""
def restoreBinaryTree(inorder, preorder):
    if not inorder or not preorder:
        return None
    
    root_value = preorder[0]
    root = TreeNode(root_value)
    
    root_index = inorder.index(root_value)
    
    root.left = restoreBinaryTree(inorder[:root_index], preorder[1:root_index+1])
    root.right = restoreBinaryTree(inorder[root_index+1:], preorder[root_index+1:])
    
    return root

"""
===============================================================================
                                MORE PYTHON SPECIFIC
===============================================================================
"""

# Problem 61: Line Encoding
"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters for example, "aabbbc" is divided into ["aa", "bbb", "c"]

Second, each substring with length greater than one is replaced with a concatenation of its length and the repeating character for example, substring "bbb" is replaced by "3b"

Finally, all the new strings are concatenated together in the same order and a new string is returned.

Example:
For s = "aabbbc", the output should be solution(s) = "2a3bc".
"""
def lineEncoding(s):
    if not s:
        return ""
    
    result = ""
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += current_char
            current_char = s[i]
            count = 1
    
    if count > 1:
        result += str(count)
    result += current_char
    
    return result

# Problem 62: Digit Degree
"""
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example:
For n = 91, the output should be solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
"""
def digitDegree(n):
    if n < 10:
        return 0
    
    degree = 0
    current = n
    
    while current >= 10:
        digit_sum = sum(int(digit) for digit in str(current))
        current = digit_sum
        degree += 1
    
    return degree

# Problem 63: Bishop and Pawn
"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

Example:
For bishop = "a1" and pawn = "c3", the output should be solution(bishop, pawn) = true.
"""
def bishopAndPawn(bishop, pawn):
    bishop_col = ord(bishop[0]) - ord('a')
    bishop_row = int(bishop[1]) - 1
    pawn_col = ord(pawn[0]) - ord('a')
    pawn_row = int(pawn[1]) - 1
    
    return abs(bishop_col - pawn_col) == abs(bishop_row - pawn_row)

# Problem 64: Is Beautiful String
"""
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example:
For inputString = "bbbaacdafe", the output should be solution(inputString) = true.
"""
def isBeautifulString(inputString):
    from collections import Counter
    counts = Counter(inputString)
    
    for i in range(1, 26):
        current_char = chr(ord('a') + i)
        prev_char = chr(ord('a') + i - 1)
        
        if counts[current_char] > counts[prev_char]:
            return False
    
    return True

# Problem 65: Find Email Domain
"""
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, allows for a lot of different special characters.

Given a valid email address, find its domain part.

Example:
For address = "prettyandsimple@example.com", the output should be solution(address) = "example.com".
"""
def findEmailDomain(address):
    return address.split('@')[-1]

# Problem 66: Build Palindrome
"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example:
For st = "abcdc", the output should be solution(st) = "abcdcba".
"""
def buildPalindrome(st):
    def is_palindrome(s):
        return s == s[::-1]
    
    if is_palindrome(st):
        return st
    
    for i in range(len(st)):
        suffix = st[i:]
        if is_palindrome(suffix):
            prefix = st[:i]
            return st + prefix[::-1]
    
    return st + st[:-1][::-1]

# Problem 67: Elections Winners
"""
Elections are in progress! Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

Example:
For votes = [2, 3, 5, 2] and k = 3, the output should be solution(votes, k) = 2.
"""
def electionsWinners(votes, k):
    max_votes = max(votes)
    max_count = votes.count(max_votes)
    
    if k == 0:
        return 1 if max_count == 1 else 0
    
    winners = 0
    for vote in votes:
        if vote + k > max_votes:
            winners += 1
    
    return winners

# Problem 68: Is MAC48 Address
"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9, A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example:
For inputString = "00-1B-63-84-45-E6", the output should be solution(inputString) = true.
"""
def isMAC48Address(inputString):
    parts = inputString.split('-')
    if len(parts) != 6:
        return False
    
    for part in parts:
        if len(part) != 2:
            return False
        if not all(c in '0123456789ABCDEF' for c in part):
            return False
    
    return True

# Problem 69: Is Digit
"""
Determine if the given character is a digit or not.

Example:
For symbol = '0', the output should be solution(symbol) = true;
For symbol = '-', the output should be solution(symbol) = false.
"""
def isDigit(symbol):
    return symbol.isdigit()

# Problem 70: Is MAC48 Address
"""
Determine if the given string is a valid MAC48 address.

Example:
For inputString = "00-1B-63-84-45-E6", the output should be solution(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be solution(inputString) = false;
For inputString = "not a MAC-48 address", the output should be solution(inputString) = false.
"""
def isMAC48Address(inputString):
    parts = inputString.split('-')
    if len(parts) != 6:
        return False
    
    for part in parts:
        if len(part) != 2:
            return False
        if not all(c in '0123456789ABCDEF' for c in part):
            return False
    
    return True

"""
===============================================================================
                                HELPER CLASSES
===============================================================================
"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

