def solution(X, A):
    st = set()
    for i, a in enumerate(A):
        if a <= X:
            st.add(a)
        if len(st) == X:
            return i
    return -1


A = [0] * 8
A[0] = 1
A[1] = 3
A[2] = 1
A[3] = 4
A[4] = 2
A[5] = 3
A[6] = 5
A[7] = 4

print(solution(5, A))
