# Reverse String Manually — iterate backwards and concatenate
# Time: O(n^2)  — string concatenation in a loop is O(n) per step in CPython
# Space: O(n)   — stores the reversed string
# Note: Use list + ''.join() for true O(n) time


original_string = "hello"
reversed_string = ""
# Time: O(n^2) due to string immutability — each += creates a new string
for i in range(len(original_string) - 1, -1, -1):
    reversed_string += original_string[i]

print(reversed_string)   # Output: "olleh"

# Efficient alternative — O(n) time:
# reversed_string = ''.join(reversed(original_string))
