# 10

def solution(arr):
    arr.remove((min(arr)))
    return arr

# 테스트 케이스
print(solution([4, 3, 2, 1]))