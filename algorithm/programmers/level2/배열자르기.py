# 처음 작성한 python 코드. 시간초과라 실패!
def solution(n, left, right):
    answer = []
    matrix = [[i+1 for i in range(n)] for _ in range(n)]
    for i in range(n):
        j=0
        while i > j:
            matrix[i][j] = i+1
            j+=1
    for i in range(n):
        answer.extend(matrix[i])
        
    return answer[left: right+1]

# 패턴을 발견했다. 노션 페이지에 설명 참고!
def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        s,r = divmod(i, n)
        if s >= r: answer.append(s+1)
        else: answer.append(r+1) 
    return answer