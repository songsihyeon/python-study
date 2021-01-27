# 5

def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a, b+1))

# 테스트 케이스
print(solution(3, 5))