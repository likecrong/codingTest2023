# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/92335
from collections import deque
def checkPrime(n): # 소수를 판별하는 함수
    if n<=1: # 1이하의 수는 소수가 아님
        return False # 거짓 반환
    for i in range(2,int(n**(1/2))+1): # 실패 원인 : n//2가 아니라 제곱근+1로 설정 해야 한다.
        if n%i == 0: # 1개라도 나누어 떨어지는 수가 존재한다면
            return False # 거짓 반환
    return True # 모든 조건을 통과했음으로 참 반환
def solution(n, k): # 3<=K<=10 : 10진수 까지 계산
    answer = 0 # 조건에 맞는 소수의 개수
    queue = deque() # n을 k진수로 변환한 큐

    # step1 : k진수 계산
    while True:
        if n<k:
            queue.appendleft(n)
            break
        elif n==k:
            queue.appendleft(n//k)
            break
        else:
            queue.appendleft(n%k)
        n //= k
        pass

    # step2 : 마지막 원소에 0 추가 -> 변환한 수의 마지막을 표기
    queue.append(0)
    # print(queue)

    # step3 : 변환수 내 0을 사이에 둔 수가 소수인지 확인
    tmp = '' # 변환수 내 0을 사이에 둔 수 저장
    while queue:
        target = queue.popleft() # 한 원소씩 반환
        if target != 0 : # 0이 아니면
            tmp += str(target) # 문자열 형태로 축적
        else: # 0이면
            #print(tmp)
            if len(tmp) == 0: # 축적된 문자가 비었을 경우
                continue # 처음으로
            if checkPrime(int(tmp)): # 축적된 문자가 소수일 경우
                answer+=1 # 개수 추가
            tmp = '' # 초기화
        pass
    return answer
if __name__ == '__main__':
    n = 437674
    k = 3
    # result 3

    n = 110011
    k = 10
    # result 2

    print(solution(n, k))
