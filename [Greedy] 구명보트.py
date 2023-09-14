# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque
# 두번째 풀이 : people을 내림차순으로 정렬하여, 첫 원소와 마지막 원소를 연산해 조건 탐색
# 성공
def solution(people, limit):
    queue = deque(people) # popleft연산과 시간복잡도 개선을 위해 people 리스트를 deque로 설정
    sortedQueue = deque(sorted(queue,reverse=True)) # 내림차순 정렬
    #print(sortedQueue)
    answer = 0 # 필요한 구명보트의 최솟값
    while sortedQueue:
        big = sortedQueue.popleft() # 현재 큐 중 가장 큰 수 반환
        if len(sortedQueue) == 0: # 현재 큐가 비어있다면
            answer+=1 # 구명보트 수 증가
            continue # 사실상 종료
        small = sortedQueue[-1] # 현재 큐가 비어있지 않다면, 가장 작은 수 반환
        # print(big)
        # print(small)
        # print()
        if (big+small)<=limit: # 구명보트는 최대 2인 탑승가능, 가장 큰 수와 작은 수를 더해 제한 확인
            sortedQueue.pop() # 현재 큐에서 가장 작은 수 삭제 (덧셈 연산에 사용됬기 때문)
        answer+=1 # 구명코트 수 증가
    return answer # 최종 구명보트 수 반환

# 첫번째 풀이 : people을 오름차순으로 정렬하여, 앞에 두 원소들을 연산해 조건 탐색
# 실패 : 잘못된 알고리즘
'''
def solution(people, limit):
    queue = deque(people)
    sortedQueue = deque(sorted(queue))
    answer = 1
    curWeight = 0
    count = 0
    while sortedQueue:
        target = sortedQueue.popleft()
        # print('sortedQueue ', sortedQueue)
        # print('curWeight', curWeight)
        # print('target', target)
        # print('count',count)
        # print()
        if (curWeight+target) <= limit and count<2:
            curWeight+=target
            count+=1
        else:
            answer+=1
            curWeight=target
            count=1
    return answer
'''
if __name__ == '__main__':
    people = [70, 50, 80, 50]
    limit = 100
    # return 3

    people = [70, 80, 50]
    limit = 100
    # return 3
    
    people = [40, 40, 40]
    limit = 40
    # return

    people = [40, 41, 42]
    limit = 45
    # return

    people = [30, 35, 35, 100]
    limit = 100
    # return 3

    people = [99,99,1,1,1,1,1,1]
    limit = 100
    # return 4

    print(solution(people, limit))
