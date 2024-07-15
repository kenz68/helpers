from typing import List


def getRow(rowIndex: int) -> List[int]:
    output = [1] * (rowIndex + 1)
    c = 0
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            output[j] += output[j - 1]
            c += 1
    print(f"Number of iterations: {c}")
    return output

# The time complexity of this function is O(n^2), where n is the rowIndex.
# This is because there are two nested loops: the outer loop runs from 2 to rowIndex,
# and the inner loop runs from i-1 to 0. Therefore, the total number of iterations
# is roughly (rowIndex * (rowIndex + 1)) / 2, which is proportional to n^2.
# The space complexity of this function is O(n), as the output list has a length of rowIndex + 1.

if __name__ == "__main__":
    rows = getRow(11)
    print(rows)
