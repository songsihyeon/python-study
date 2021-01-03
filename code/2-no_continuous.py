# 2

def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i] : continue
        a.append(i)
    return a

# 테스트 케이스
print(solution("1122233"))
