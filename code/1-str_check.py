# 1

def solution(s) :
    return s.isdigit() and len(s) in (4, 6)

# 테스트 케이스
print(solution("a234"))
print(solution("1254"))
