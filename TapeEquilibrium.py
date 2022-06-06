def solution(A):
    sum_a = sum(A)
    min_diff = float('inf')
    left = 0
    for i in range(len(A) - 1):
        left += A[i]
        sum_a -= A[i]
        current_dif = abs(left - sum_a)
        if min_diff > current_dif:
            min_diff = current_dif
    return min_diff


A = [0] * 5
A[0] = 3
A[1] = 1
A[2] = 2
A[3] = 4
A[4] = 3
print(solution(A))
