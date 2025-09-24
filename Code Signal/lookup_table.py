# Given an array of unique integers numbers, your task is to find the number of pairs of indices (i, j) such that i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2.

# Note: The numbers 2^0  = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, etc. are considered to be powers of 2.


from collections import defaultdict

 def solution(numbers):
   counts = defaultdict(int)
   answer = 0
   for element in numbers:
       counts[element] += 1
       for two_power in range(21):
           second_element = (1 << two_power) - element
           answer += counts[second_element]
   return answer 
