import sys

result = set()

fast_input = sys.stdin.readline

for _ in range(10):
    result.add(int(fast_input()) % 42)

print(len(result))
