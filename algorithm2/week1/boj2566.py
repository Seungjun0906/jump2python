# 백준 2566
# https://www.acmicpc.net/problem/2566
# 완전 탐색
import sys

fast_input = sys.stdin.readline

arr = [list(map(int, fast_input().split())) for _ in range(9)]

max = arr[0][0]
a = 0
b = 0

for i in range(9):
    for j in range(9):
        print("i", i)
        print("j", j)
        if arr[i][j] > max:
            max = arr[i][j]
            a, b = i, j
        else:
            continue

print(max)
print(f"{a + 1} {b + 1}")
