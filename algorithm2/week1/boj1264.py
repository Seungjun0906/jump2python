# BOJ 1264
# https://www.acmicpc.net/problem/1264


import sys

fast_input = sys.stdin.readline

모음 = ["a", "e", "i", "o", "u"]  # O(1)

arr = []  # O(1)

while True:
    # 소문자 치환 및 문장의 양끝 공백 제거
    phrase = fast_input().lower().strip()  # O(m) + O(m) + O(m)

    # #를 만나면 탈출
    if phrase == "#":
        break
    else:
        arr.append(phrase)


for row in arr:  # O(n)
    cnt = 0  # O(1)
    for char in row:  # O(m)
        if char in 모음:  # 최악의 경우 O(5) => O(1)
            cnt += 1  # O(1)
    print(cnt)


# 풀이 2
# import sys

# fast_input = sys.stdin.readline
# 모음 = {"a", "e", "i", "o", "u"}  # Set을 사용하여 조회 속도 O(1)로 개선

# while True:
#     phrase = fast_input().strip().lower()  # 입력을 받고 바로 처리
#     if phrase == "#":
#         break

#     cnt = sum(
#         1 for char in phrase if char in 모음
#     )  # 리스트 안 쓰고 한 줄에서 바로 처리
#     print(cnt)
