def solution(A):
    zeros = 0
    count = 0
    for a in A:
        zeros += 1 if a == 0 else 0
        count += zeros if a == 1 else 0
        if count > 1000000000:
            return -1
    return count


A = [0] * 5
A[0] = 0
A[1] = 1
A[2] = 0
A[3] = 1
A[4] = 1
print(solution(A))
