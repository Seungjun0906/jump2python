import sys

fast_input = sys.stdin.readline

N, X = map(int, fast_input().split())

text = ""

for num in [n for n in list(map(int, fast_input().split()))]:
    if num < X:
        text += " " + str(num)

print(text)
