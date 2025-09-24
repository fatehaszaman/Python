# Generate an n x n Star BoxProblem DescriptionGiven an integer n, return an n x n box made of asterisks (*) for the border, with spaces inside. 
# The box is returned as a list of strings, where each string represents a row.Examples


def generate_box(n):
    if n < 2:
        return []
    
    box = []
    for i in range(n):
        if i == 0 or i == n - 1:
            # Top and bottom rows: all stars
            row = '*' * n
        else:
            # Middle rows: star + spaces + star
            row = '*' + ' ' * (n - 2) + '*'
        box.append([row])  # Each row as a list with one string
    return box

# Test Examples
print(generate_box(4))  # [["****"], ["*  *"], ["*   *"], ["****"]]
print(generate_box(2))  # [["**"], ["**"]]
