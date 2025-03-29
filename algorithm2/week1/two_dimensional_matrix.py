target = 5

import sys

fast_input = sys.stdin.readline

N, M = map(int, fast_input().split())  # N * M 행렬
matrix = [list(map(int, fast_input().split())) for _ in range(N)]


has_target = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            has_target = True
            break

print(has_target)
