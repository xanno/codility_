def solution(S, P, Q):
    res = [0] * len(P)
    for i in range(len(P)):
        if "A" in S[P[i]:Q[i] + 1]:
            res[i] = 1
        elif "C" in S[P[i]:Q[i] + 1]:
            res[i] = 2
        elif "G" in S[P[i]:Q[i] + 1]:
            res[i] = 3
        else:
            res[i] = 4

    return res


S = 'CAGCCTA'
Q = [0] * 3
P = [0] * 3
P[0] = 2
Q[0] = 4
P[1] = 5
Q[1] = 5
P[2] = 0
Q[2] = 6
print(solution(S, P, Q))
print(solution('GT', [0, 0, 1], [0, 1, 1]))
