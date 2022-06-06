def solution(N):
    number_binary = bin(N)[2:]
    count = 0
    res = 0
    for c in number_binary:
        if c == '0':
            count += 1
        if c == '1':
            res = max(count, res)
            count = 0
    return res


print(solution(15))
print(solution(1041))
print(solution(32))

