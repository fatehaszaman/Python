# CodeSignal — Lookup Table / Power-of-Two Pairs
# Count pairs (i, j) with i <= j where numbers[i] + numbers[j] is a power of 2.
# Time: O(n * log(max_val))  — for each element check 21 possible powers of 2
# Space: O(n)                — frequency hash map

from collections import defaultdict


# Time: O(n * 21) = O(n) | Space: O(n)
def solution(numbers):
    counts = defaultdict(int)
    answer = 0
    for element in numbers:
        counts[element] += 1
        for two_power in range(21):           # 2^0 to 2^20 covers up to ~10^6
            second_element = (1 << two_power) - element
            answer += counts[second_element]  # count how many prior elements pair up
    return answer
