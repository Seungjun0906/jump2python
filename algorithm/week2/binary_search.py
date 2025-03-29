import sys

input = sys.stdin.readline

target_num = 14

num_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def binary_search(num_arr, target_num):
    cur_min = 0
    cur_max = len(num_arr) - 1
    cur_guess = (cur_min + cur_max) // 2

    cnt = 0

    while cur_min <= cur_max:
        cnt += 1
        print(cur_guess)
        if num_arr[cur_guess] == target_num:
            return True
        elif num_arr[cur_guess] < target_num:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1

        cur_guess = (cur_min + cur_max) // 2


binary_search(num_arr, 7)
