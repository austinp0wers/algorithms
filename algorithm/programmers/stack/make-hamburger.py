def solution(ingredient):
    if len(ingredient) < 1:
        return 0
    result = 0
    stack = []
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if stack[-4:] == [1,2,3,1]:
            for _ in range(4):
                stack.pop()
            result+=1
        
    return result