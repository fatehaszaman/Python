#Given an array a, your task is to output an array b of the same length by applying the following transformation: 
# For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
# For instance, b[0] = 0 + a[0] + a[1]


# For Example
# For a = [4, 0, 1, -2, 3]: 
# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

# So, the output should be solution(a) = [4, 5, -1, 2, 1]

def solution(a):
   n = len(a)
   b = [0 for _ in range(n)]
   for i in range(n):
       b[i] = a[i]
       if i > 0:
           b[i] += a[i - 1]
       if i < n - 1:
           b[i] += a[i + 1]
   return b 

# Test the function
if __name__ == "__main__":
    # Test with the example from the comments
    a = [4, 0, 1, -2, 3]
    result = solution(a)
    print(f"Input: {a}")
    print(f"Output: {result}")
    
    # Additional test cases
    test_cases = [
        [1, 2, 3, 4, 5],
        [1],
        [1, 2],
        [0, 0, 0, 0]
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = solution(test)
        print(f"Test {i}: {test} -> {result}")
