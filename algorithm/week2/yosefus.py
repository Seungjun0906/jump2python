# import sys

# def solution (N:int, K:int):
#     list_ = list(range(1 , N  + 1))
#     cur_seq = 0
#     result = []
    
#     while len(list_) > 0:
#         if(cur_seq > K - 2):
#             cur_seq = 0
#             result.append(str(list_.pop(0)))
#         else:
#             cur_seq += 1
#             list_.append(str(list_.pop(0)))

#     text = ", ".join(result)
        
#     print("<" + text + ">")

# def withQ (n:int, k:int) -> int:
#     q = [i for i in range(1, n+1)]

#     while len(q) > 1:
#         for j in range(1, k + 1):
#             friend = q.pop(0)
            
#             if j != k
    



# fast_input = sys.stdin.readline

# [N, K] = fast_input().split()

# # solution(int(N),int(K))
# withQ(N,K)


# 큐를 이용하는 방법

def findTheWinner(n:int, k:int) -> int:
    q = [i for i in range(1, n+1)]
    
    while len(q) > 1:
        for j in range(1, k + 1):
            friend = q.pop(0)
            if j != k:
                q.append(friend)
    return q[0] 

def findTheWinnerWithCircularLinkedList(n:int, k:int) -> int:
    q = [i for i in range(1 , n + 1)]
    j = 0

    while len(q) > 1:
        j = (j + k - 1) % len(q)
        q.pop(j)

    return q[0]


def findTheWinnerWithRecursive(n:int, k:int) -> int:
    if n == 1: 
        return 1
    return (findTheWinnerWithRecursive(n - 1, k) + k - 1) % n + 1