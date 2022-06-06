def solution(N, A):
    arr = [0] * N
    max_counter = 0
    is_max = False
    current_max = 0
    for a in A:
        if a <= N:
            if is_max:
                arr[a - 1] = max(arr[a - 1], max_counter)
            arr[a - 1] += 1
            current_max = max(current_max, arr[a - 1])
        if a > N:
            is_max = True
            max_counter = current_max

    if is_max:
        for i, a in enumerate(arr):
            arr[i] = max(a, max_counter)
    return arr


A = [0] * 7
A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4
print(solution(5, A))
