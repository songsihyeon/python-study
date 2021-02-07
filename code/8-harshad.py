# 8

def solution(x):
    return x % sum(int(n) for n in str(x)) == 0

# 테스트 케이스
print(solution(10))