# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12985
'''
    배경 : n명이 참가하는 토너먼트 (n은 2의 지수승)
    문제 : a 참가자와 b 참가자가 만나는 라운드 반환
    특징 : a 참가자와 b 참가자가 서로 붙기 전까지 항상 이김 (a와 b는 다른 자연수)
'''
def solution(n,a,b):
    # 첫번째 참가자가 1번임으로 0번부터 활용하기 위한 연산
    a -= 1
    b -= 1
    
    # 예외처리 : left보다 right보다 반드시 작음
    if a>b:
        left = b
        right = a
    else:
        left = a
        right = b
    
    count=0 # 몇번째 라운드에서 만나는지 반환
    while True:
        
        # a와 b가 만나는 라운드 조건
        if left%2==0: # 왼쪽이 짝수라면
            if left+1 == right: # 반드시, 오른쪽이 왼쪽보다 1큼
                break # 종료
                
        # 다음 라운드 연산
        # 각 2팀 중 1팀 진출
        left //= 2 
        right //= 2
        count+=1
        
    return count+1 # 정답 반환

if __name__ == '__main__':
    n = 8
    a = 4
    b = 7
    # answer 3

    n = 2
    a = 1
    b = 2
    # answer 1

    n = 8
    a = 2
    b = 3
    # answer 2

    print(solution(n,a,b))
