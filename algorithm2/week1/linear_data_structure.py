# import sys

# fast_input = sys.stdin.readline

# arr_2D = [
#     list(map(lambda x: int(x) if x.isdigit() else x, fast_input().split()))
#     for _ in range(4)
# ]

# print(arr_2D)

# # 이름순으로 정렬하기
# sorted_by_name = sorted(arr_2D)
# # 점수를 기준으로
# sorted_by_score = sorted(arr_2D, key=lambda x: x[1], reverse=True)
# # 학점을 기준으로
# sorted_by_score2 = sorted(arr_2D, key=lambda x: x[2])

# print("이름순", sorted_by_name, sep="\n")
# print("점수", sorted_by_score, sep="\n")
# print("학점순", sorted_by_score2, sep="\n")

# import sys

# fast_input = sys.stdin.readline

# N = int(fast_input())

# result = []

# for _ in range(N):
#     A, B = map(int, fast_input().split())
#     result.append(A + B)

# for num in result:
#     print(num)
