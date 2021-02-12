# 13

def solution(n, m):
    def gcd(n,m):
        while(m):
            n,m = m,n%m
        return n
    return [gcd(n,m), n*m/gcd(n,m)]

# 테스트 케이스
print(solution(3,12))