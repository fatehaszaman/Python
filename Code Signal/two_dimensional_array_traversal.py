# CodeSignal — 2D Array Traversal / Figure Dropping
# Find column position to drop a 3x3 figure so at least one full row is formed.
# Time: O(W * H * F^2)  — W columns * H rows * F^2 figure cells (F = figure_size = 3)
#                          Simplifies to O(W * H) since F is constant
# Space: O(1)            — only index variables, no extra structures


# Time: O(W * H) | Space: O(1)
def solution(field, figure):
    height = len(field)
    width = len(field[0])
    figure_size = len(figure)

    for column in range(width - figure_size + 1):
        # Drop figure as low as possible in this column
        row = 1
        while row < height - figure_size + 1:
            can_fit = True
            for dx in range(figure_size):
                for dy in range(figure_size):
                    if field[row + dx][column + dy] == 1 and figure[dx][dy] == 1:
                        can_fit = False
            if not can_fit:
                break
            row += 1
        row -= 1   # last valid row

        # Check if any row becomes fully filled
        for dx in range(figure_size):
            row_filled = True
            for column_index in range(width):
                if not (field[row + dx][column_index] == 1 or
                        (column <= column_index < column + figure_size and
                         figure[dx][column_index - column] == 1)):
                    row_filled = False
            if row_filled:
                return column

    return -1
