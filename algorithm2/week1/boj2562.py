import sys

fast_input = sys.stdin.readline

idx = None
num = None

for i in range(1, 10):
    num_from_input = int(fast_input())
    if i == 1:
        idx = i
        num = num_from_input
        continue

    if num_from_input > num:
        num = num_from_input
        idx = i

print(num)
print(idx)
