def solution(A):
    st = set()
    for a in A:
        st.add(a)
    for i in range(1, len(A) + 2):
        if i not in st:
            return i


A = [0] * 4
A[0] = 2
A[1] = 3
A[2] = 1
A[3] = 5
print(solution(A))
