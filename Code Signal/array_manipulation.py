# CodeSignal — Array Manipulation
# For each element, replace it with the sum of itself and its neighbours.
# Time: O(n)   — single pass through array
# Space: O(n)  — output array of same length

# Example: a = [4, 0, 1, -2, 3] -> [4, 5, -1, 2, 1]


# Time: O(n) | Space: O(n)
def solution(a):
    n = len(a)
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
        if i > 0:
            b[i] += a[i - 1]   # add left neighbour
        if i < n - 1:
            b[i] += a[i + 1]   # add right neighbour
    return b


if __name__ == "__main__":
    a = [4, 0, 1, -2, 3]
    print(f"Input:  {a}")
    print(f"Output: {solution(a)}")

    test_cases = [[1, 2, 3, 4, 5], [1], [1, 2], [0, 0, 0, 0]]
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test} -> {solution(test)}")
