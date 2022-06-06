def solution(A, B, K):
    A = A if A % K == 0 else A + (K - A % K)
    B = B - B % K
    return (B - A) // K + 1


print(solution(6, 11, 2))
print(solution(11, 345, 17))
