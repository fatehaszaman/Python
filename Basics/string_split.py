# str.split() — split a string by a delimiter
# Time: O(n)   — scans every character once to find delimiters
# Space: O(n)  — result list stores all substrings

string = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
# Time: O(n) | Space: O(n)
print(string.split("."))

# Output:
# ['Tell me and I forget', ' Teach me and I remember', ' Involve me and I learn', '']
