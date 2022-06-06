def solution(A):
    st = set()
    for a in A:
        st.add(a)

    for i in range(1, 1000001):
        if i not in st:
            return i

    return -1


A = [1, 3, 6, 4, 1, 2]
print(solution(A))
a = [-1, -3]
print(solution(a))
