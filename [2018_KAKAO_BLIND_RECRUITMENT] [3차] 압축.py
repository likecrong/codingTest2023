# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

from collections import deque
def solution(msg):
    answer = [] # 출력된 색인번호 리스트
    data = {} # 영어 대문자 색인 사전
    wait = deque() # 대기 큐
    cur = deque(msg) # 현재 큐, 매개변수(문자열)을 원소로 초기화
    last = 27 # 현재 색인

    # 1. 영어 대문자 A~Z 색인 사전 생성
    for i in range(1, last):
        data[(chr(65+i-1),)] = i # 튜플을 활용해 KEY 설정

    # 2. LZW 압축
    while len(wait)>0 or len(cur)>0: # 대기큐와 현재큐 모두 비울 때 까지   
        tcur = tuple(cur) # 현재 큐 -> 튜플화 (W)
        if tcur in data.keys(): # 키 검색
            answer.append(data[tcur]) # 해당 키에 대한 색인 추가
            if len(wait)>0: # 대기큐에 원소가 있다면
                ttmp = tuple(list(cur) + list(wait[0])) # W + C
            else:
                ttmp = tuple(list(cur)) # W + 생략
            data[ttmp] = last # (W + C)에 대한 색인을 사전에 추가
            
            last+=1 # 다음 색인
            cur = wait # 현재 큐 원소는 버리고, 대기 큐 내용으로 채우기
            wait = deque() # 대기 큐 비우기
        else: # 키가 없다면
            wait.appendleft(cur.pop()) 
            # 현재 큐의 가장 오른쪽 원소를 대키 큐의 왼쪽에 밀기 
        pass
    return answer

msg = 'KAKAO'
answer = [11, 1, 27, 15]

msg = 'TOBEORNOTTOBEORTOBEORNOT'
answer = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]

msg = 'ABABABABABABABAB'
answer = [1, 2, 27, 29, 28, 31, 30]

print(solution(msg))
