def solution(A, K):
    new_a = [0] * len(A)
    for i in range(len(A)):
        new_idx = (i + K) % len(A)
        new_a[new_idx] = A[i]
    return new_a


A = [3, 8, 9, 7, 6]
print(solution(A, 3))
