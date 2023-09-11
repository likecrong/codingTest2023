# 문제 링크:
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
from collections import deque
def solution(n, lost, reserve):

    # 학생 리스트 오름차순 정렬
    lost.sort()
    reserve.sort()

    '''    
    # 첫번째 풀이 : 여벌옷이 있는 학생이 옷이 없는 학생 빌려주기
    reserveQue = deque(reserve)
    while reserveQue:
        print(reserveQue)
        print(lost)
        target = reserveQue.popleft()
        a, b = target-1, target+1
        if a in lost:
            lost.remove(a)
            continue
        if b in lost:
            lost.remove(b)
        pass     
    return n-len(lost)    
    
    # 두번째 풀이 : 옷이 없는 학생이 여벌옷이 있는 학생에게 빌리기
    # 첫번째 풀이와 같은 케이스 실패
    lostQue = deque(lost)
    while lostQue:
        #print(lostQue)
        #print(reserve)
        target = lostQue.popleft()
        a, b = target-1, target+1
        if a in reserve:
            reserve.remove(a)
        elif b in reserve:
            reserve.remove(b)
        else:
            n-=1
        pass
    return n
    '''

    # 세번째 풀이 : 옷이 없는 학생이 여벌옷이 있는 학생에게 빌리기
    # 원인 : reserve(여벌)에 속하더라도 lost(없는)에 속한다면 빌려줄 수 없다.
    # -> 두 리스트에서 같은 원소 제거
    newlost = list(set(lost) - set(reserve))
    newReserve = list(set(reserve) - set(lost))
    #print(newlost)
    #print(newReserve)

    lostQue = deque(newlost) # 옷이 없는 학생 기준 queue
    while lostQue:
        #print(lostQue)
        #print(newReserve)
        target = lostQue.popleft() # 오름차순 순서대로
        a, b = target-1, target+1 # 자신의 앞 번호와 뒷 번호 지정

        # 탐욕법(Greedy)
        if a in newReserve: # 앞 번호 확인
            newReserve.remove(a) # 빌려줄 학생 확인 후 제거(처리완료)
        elif b in newReserve: # 뒷 번호 확인
            newReserve.remove(b) # 빌려줄 학생 확인 후 제거(처리완료)
        else: # 빌려줄 사람이 없을 경우
            n-=1 # 전체 학생 수에서 감소
        pass
    return n # 전체 학생 수 - 옷을 못빌린 학생 수

if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    # return 5

    n = 5
    lost = [2, 4]
    reserve = [3]
    # return 4

    n = 3
    lost = [3]
    reserve = [1]
    # return 2

    n = 5
    lost = [3, 5]
    reserve = [2, 4]
    # return 5

    n = 5
    lost = [2, 3, 5]
    reserve = [2, 3, 4]
    # return 5

    n = 4
    lost = [2, 3]
    reserve = [3, 4]
    # return 3

    print(solution(n, lost, reserve))
