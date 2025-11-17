"""
You are given two sequences of integers: A = {a1, a2, …. ai} and B = {b1, b2, …. bj}.
Define an algorithm that returns the longest sequence of alternating increasing values from A and B where the sequence X = {x1, x2, …. xn} is as follows:
The elements of X are increasing e.g. xi < xi+1 for all 1 <= I < n
The odd-indexed elements of X are a subsequence of one of the sequences either A or B and the even-indexed elements of X are a subsequence of the other sequence.
Note a subsequence need not be consecutive elements of the original sequence but must maintain the relative order of the original sequence
For example A = {1,7,2} and B = {4,8,3,9} then the answer is X = {4,7,9} which has a length of 3.


Demonstrate you code by running your code with the provided input files. The input file will contain 4 input lines. The first line will be the size of the A array, the second will be the size of the B array the third line will be the A array values separated by a space and the fourth line will be the B array values separated by a space.
Sample input file: 
5
6
8 2 9 1 4
4 1 5 3 2 6

You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how to run your code and you must submit screen shots of your running code. The output should be of the format:

File Input: longest_seq<input file number>.txt 
Longest Sequence: <the longest sequence you computed>
"""
def longest_alternating_sequence(A, B):
    length_a, length_b = len(A), len(B)
    dp = [[0] * (length_b + 1) for _ in range(length_a + 1)]
    max_length = 0
    end_position = (0, 0)
    next_from_A = True

    for index_a in range(length_a + 1):
        for index_b in range(length_b + 1):
            if index_a > 0 and (next_from_A or index_b == 0):
                for prev_b_index in range(index_b):
                    if A[index_a - 1] > B[prev_b_index]:
                        candidate = dp[index_a - 1][prev_b_index + 1] + 1
                        if dp[index_a][index_b] < candidate:
                            dp[index_a][index_b] = candidate
            if index_b > 0 and (not next_from_A or index_a == 0):
                for prev_a_index in range(index_a):
                    if B[index_b - 1] > A[prev_a_index]:
                        candidate = dp[prev_a_index + 1][index_b - 1] + 1
                        if dp[index_a][index_b] < candidate:
                            dp[index_a][index_b] = candidate
            if dp[index_a][index_b] > max_length:
                max_length = dp[index_a][index_b]
                end_position = (index_a, index_b)
            next_from_A = not next_from_A

    sequence = []
    index_a, index_b = end_position
    while max_length > 0:
        if next_from_A:
            for prev_b_index in range(index_b):
                if A[index_a - 1] > B[prev_b_index] and dp[index_a][index_b] == dp[index_a - 1][prev_b_index + 1] + 1:
                    sequence.append(A[index_a - 1])
                    index_a -= 1
                    index_b = prev_b_index + 1
                    max_length -= 1
                    break
        else:
            for prev_a_index in range(index_a):
                if B[index_b - 1] > A[prev_a_index] and dp[index_a][index_b] == dp[prev_a_index + 1][index_b - 1] + 1:
                    sequence.append(B[index_b - 1])
                    index_b -= 1
                    index_a = prev_a_index + 1
                    max_length -= 1
                    break
        next_from_A = not next_from_A

    return sequence[::-1]



if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    size_a = int(data[0])
    size_b = int(data[1])
    A = list(map(int, data[2].split()))
    B = list(map(int, data[3].split()))
    
    result = longest_alternating_sequence(A, B)
    print(f"Longest Sequence: {' '.join(map(str, result))}")