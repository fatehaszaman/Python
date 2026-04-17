# Generate n x n Star Box — hollow square border of asterisks
# Time: O(n)    — create n rows, each O(n) string construction -> O(n^2) overall
# Space: O(n^2) — output list stores n strings of up to n characters each


# Time: O(n^2) | Space: O(n^2)
def generate_box(n):
    if n < 2:
        return []

    box = []
    for i in range(n):
        if i == 0 or i == n - 1:
            row = '*' * n          # top and bottom rows: all stars
        else:
            row = '*' + ' ' * (n - 2) + '*'   # middle rows: border only
        box.append([row])
    return box


# Test Examples
print(generate_box(4))   # [["****"], ["*  *"], ["*   *"], ["****"]]
print(generate_box(2))   # [["**"], ["**"]]
