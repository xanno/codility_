def solution(A):
    idx = 0
    min_avg = float('inf')
    odd_slice = float('inf')
    for i in range(len(A) - 1):
        sum_two = A[i] + A[i + 1]
        even_slice = sum_two / 2
        if i + 2 < len(A):
            odd_slice = (sum_two + A[i + 2]) / 3
        if min_avg > even_slice or min_avg > odd_slice:
            min_avg = min(min_avg, even_slice, odd_slice)
            idx = i
    return idx


A = [0] * 7
A[0] = 4
A[1] = 2
A[2] = 2
A[3] = 5
A[4] = 1
A[5] = 5
A[6] = 8
print(solution(A))
