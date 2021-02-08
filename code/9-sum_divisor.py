# 9

def solution(n): 
    return sum([i for i in range(1, n+1) if n % i == 0])

# 테스트 케이스
print(solution(12))