def solution(A):
    occ = set()
    for a in A:
        if a in occ:
            return 0
        occ.add(a)
    for i in range(1, len(A) + 1):
        if i not in occ:
            return 0
    return 1


A = [0] * 4
A[0] = 4
A[1] = 1
A[2] = 3
A[3] = 2
print(solution(A))
print(solution([4, 1, 3]))
