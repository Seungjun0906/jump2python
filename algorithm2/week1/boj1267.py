import sys

# 영식 요금
# 30초 마다 10원
# 0~30 10

# 민식 요금
# 0 ~ 60 15


fast_input = sys.stdin.readline

# 영식 Y
charge_per_time_Y = 10

seconds_Y = 30

# 민식 M
charge_per_time_M = 15

seconds_M = 60


N = int(fast_input())

time_arr = list(map(int, fast_input().split()))[:N]

total_charge_Y = 0
total_charge_M = 0

for time in time_arr:
    # 나누어 떨어진다면
    if time % seconds_Y == 0:
        total_charge_Y += ((time // seconds_Y) + 1) * charge_per_time_Y
    else:
        total_charge_Y += ((time // seconds_Y) + 1) * charge_per_time_Y

    # 나누어 떨어진다면
    if time % seconds_M == 0:
        total_charge_M += ((time // seconds_M) + 1) * charge_per_time_M
    else:
        total_charge_M += ((time // seconds_M) + 1) * charge_per_time_M


if total_charge_M == total_charge_Y:
    print(f"Y M {total_charge_M}")
elif total_charge_Y > total_charge_M:
    print(f"M {total_charge_M}")
else:
    print(f"Y {total_charge_Y}")
