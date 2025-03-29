import sys

# 무작위 수 찾기

input = sys.stdin.readline

# 넘버들
num_arr = list(map(int, input().split(" ")))
# 타겟
target = int(input())


def is_exisit_target_number_binary(target_num: int, arr: list[int]) -> bool:
    arr.sort()
    min_idx = 0
    max_idx = len(arr) - 1
    cur_target_idx = (min_idx + max_idx) // 2

    while min_idx <= max_idx:
        cur_value = arr[cur_target_idx]
        print("= = == = = = = = =")
        print(cur_value)
        print(target)
        print("= = == = = = = = =")
        if cur_value == target:
            return True
        elif cur_value < target_num:
            min_idx = cur_target_idx + 1

        elif cur_value > target_num:
            max_idx = cur_target_idx - 1

        cur_target_idx = (min_idx + max_idx) // 2

    return False


result = is_exisit_target_number_binary(target_num=target, arr=num_arr)

print(result)
