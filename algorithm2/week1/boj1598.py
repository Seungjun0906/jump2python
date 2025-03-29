import sys

fast_input = sys.stdin.readline
# 랜덤 두 개의 자연수
A, B = list(map(int, fast_input().split()))


def calc_vertical(num):
    remainder = num % 4
    if remainder == 0:
        return 4
    else:
        return remainder


def calc_horizontal(num):
    remainder = num % 4
    if remainder == 0:
        return (num // 4) - 1
    else:
        return num // 4


vertical_a = calc_vertical(A)

vertical_b = calc_vertical(B)

horizontal_a = calc_horizontal(A)

horizontal_b = calc_horizontal(B)

print(abs(vertical_a - vertical_b) + abs(horizontal_a - horizontal_b))

# A 와 B 사이의 거리
# 첫줄 x % 4 = 1
# 둘째 줄 x % 4 = 2
# 셋째 줄 x % 4 = 3
# 넷째 줄 x % 4 = 0

# 가로로
#  // 4   0 1 2 3 4 5 6 ;;;;;


# 가로 차이
# 11 // 4 = 2
# 33 // 4 = 8

# 새로 차이
# 11 % 4 = 3
# 33 % 4 = 1

# 가로
