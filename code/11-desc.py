# 11

def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    return int("".join(n))

# 테스트 케이스
print(solution(41538))