import sys

fast_input = sys.stdin.readline

N, M = map(int, fast_input().split())

maxtrix1 = [list(map(int, fast_input().split())) for _ in range(N)]

maxtrix2 = [list(map(int, fast_input().split())) for _ in range(N)]

new_matrix = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    for j in range(M):
        new_matrix[i][j] = str(maxtrix1[i][j] + maxtrix2[i][j])


for row in new_matrix:
    print(" ".join(row))
