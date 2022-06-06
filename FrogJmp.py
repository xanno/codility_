import math


def solution(X, Y, D):
    return int(math.ceil((Y - X) / D))


print(solution(10, 85, 30))
