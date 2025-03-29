# import sys

# fast_input = sys.stdin.readline

# N = int(fast_input())

# str_arr = [word for word in [fast_input().rstrip() for _ in range(N)]]

# cnt = 0

# for word in str_arr:
#     map: dict = {}
#     cur_char = ""

#     for char in word:
#         # 현재 탐색중인 알파벳과 cur_char가 같다면 같은지 확인한다
#         # 같다면 continue
#         if char == cur_char:
#             continue

#         val = map.get(char)

#         # 같지 않다면 같지 않다면 현재 dict에 현재 알파벳을 키로 가진 값이 Trthy한지 판단
#         # 이 말은 이미 한 번 탐색했는데 나중에 다시 나왔다는 말이므로 연속하지 않는 문자열이므로 break
#         if char != cur_char and val:
#             map.update({char: False})
#             break

#         # 같지 않고 dict에 현재 알파벳을 키로 가진 값이 Falsy하면 map[char] = True로  cur_char = char로 변경
#         if char != cur_char and not val:
#             map.update({char: True})
#             cur_char = char
#     # False가 하나라도 존재한다면 다음 단어로 넘어가야함
#     if False in map.values():
#         continue

#     cnt += 1

# print(cnt)


import sys

fast_input = sys.stdin.readline

N = int(fast_input())
cnt = 0

for _ in range(N):
    word = fast_input().rstrip()
    prev_char = None
    is_group_word = True
    seen = set()

    for char in word:
        if char != prev_char:
            if char in seen:
                is_group_word = False
                break

            seen.add(char)

        prev_char = char

    if is_group_word:
        cnt += 1


print(cnt)
