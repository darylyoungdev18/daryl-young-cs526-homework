"""

You are a downhill skier looking for an adventure. You will be dropped by helicopter as a location of your choosing on a mountain. The mountain is represented as an m x n matric of altitude values. Design an algorithm that determines the longest path you can follow down the mountain such that each successive cell in your path has an altitude lower than the previous cell. 
Note: Each Cell has up to eight neighbors, directly adjacent horizontally, vertically or diagonally.
Output the longest path to the terminal.

You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how to run your code and you must submit screen shots of your running code on all provided inputs and printing your result to the console.


Sample input:
4
5
4 8 7 9 8
6 5 10 12 11
3 6 15 11 12
1 4 9 13 10

python3 ski.py < ski-inputs/ski_input1.txt 
9

"""
import sys
from pathlib import Path
sys.setrecursionlimit(10000)
def longest_path_from_cell(matrix, x, y, memo):
    if (x, y) in memo:
        return memo[(x, y)]

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    max_length = 1  # At least the cell itself

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] < matrix[x][y]:
            length = 1 + longest_path_from_cell(matrix, nx, ny, memo)
            max_length = max(max_length, length)

    memo[(x, y)] = max_length
    return max_length
def find_longest_path(matrix):
    memo = {}
    max_path_length = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            path_length = longest_path_from_cell(matrix, i, j, memo)
            max_path_length = max(max_path_length, path_length)

    return max_path_length
if __name__ == "__main__":
    raw_text = ""
    input_name = "stdin"
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        input_name = input_path.name
        raw_text = input_path.read_text()
    else:
        raw_text = sys.stdin.read()

    lines = raw_text.splitlines()
    if not lines:
        print("No input provided.")
        sys.exit(1)

    m = int(lines[0].strip())
    n = int(lines[1].strip())
    matrix = []
    for i in range(2, 2 + m):
        row = list(map(int, lines[i].strip().split()))
        matrix.append(row)

    longest_path_length = find_longest_path(matrix)
    print(longest_path_length)
