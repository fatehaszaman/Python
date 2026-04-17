# CodeSignal — String Pattern Matching (vowel/consonant pattern)
# Count substrings of source matching a 0/1 vowel/consonant pattern.
# Time: O(n * m)  — for each of (n - m + 1) start positions, scan m chars
# Space: O(1)     — no extra data structures beyond the answer counter
# where n = len(source), m = len(pattern)

vowels = ['a', 'e', 'i', 'o', 'u', 'y']


# Time: O(m) per call | Space: O(1)
def check_for_pattern(pattern, source, start_index):
    for offset in range(len(pattern)):
        if pattern[offset] == '0':
            if source[start_index + offset] not in vowels:
                return 0   # expected vowel, got consonant
        else:
            if source[start_index + offset] in vowels:
                return 0   # expected consonant, got vowel
    return 1


# Time: O(n * m) | Space: O(1)
def solution(pattern, source):
    answer = 0
    for start_index in range(len(source) - len(pattern) + 1):
        answer += check_for_pattern(pattern, source, start_index)
    return answer
