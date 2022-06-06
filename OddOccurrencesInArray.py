def solution(A):
    occ = {}
    for a in A:
        occ[a] = occ.get(a, 0) + 1
    for k, v in occ.items():
        if v % 2 != 0:
            return k
    return -1


A = [0] * 7
A[0] = 9
A[1] = 3
A[2] = 9
A[3] = 3
A[4] = 9
A[5] = 7
A[6] = 9
print(solution(A))