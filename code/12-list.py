# 12

def solution(array, commands): 
    return [sorted(array[x[0]-1:x[1]])[x[2]-1] for x in commands]

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))