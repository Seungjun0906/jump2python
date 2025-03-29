import sys

input = sys.stdin.readline


# # 팩토리얼
# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial(n - 1)


# N = int(input())

# result = factorial(N)
# print(result)


text = input().replace(" ", "").strip()


# 회문검사
def is_palindrome(word: str):
    print(word[0])
    print(word[-1])

    if len(word) <= 1:
        return True

    if word[0] != word[-1]:

        return False

    return is_palindrome(word[1 : len(word) - 1])


result = is_palindrome(text)
print(result)
