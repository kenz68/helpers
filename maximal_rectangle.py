from typing import List


def maximalRectangle(matrix: List[List[str]]) -> int:
    row = len(matrix)
    col = len(matrix[0])
    m = 0
    for x in range(row):
        for y in range(col):
            if matrix[x][y] == '1':
                w, h = 1, 1

                print(f"matrix[{x}][{y}]: {matrix[x][y]}")
    return m

def isRectangle(matrix: List[List[str]], x, y, w, h: int) -> bool:
    for row_index in range(x, x + h):
        row = matrix[row_index]
        sub_row = row[y:y + w]
        if sub_row.count('1') != w:  # Ensure all rows have the same width
            return False

    return True  # If we reach here, all sub-rows have equal width


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(maximalRectangle(matrix))
