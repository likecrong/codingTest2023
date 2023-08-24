# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque
import heapq
def solution(priorities, location):
    index = deque([x for x in range(len(priorities))]) # 인덱스 큐
    newPriorities = deque(priorities) # 우선순위 큐

    count = 0 # 해당 location의 수가 몇번째로 반환되는 지 count
    while newPriorities:
        curPri = newPriorities.popleft() #현재 프로세스
        curIndex = index.popleft() #현재 프로세스의 인덱스 (location 기반)

        if len(newPriorities)==0: # 우선순위 큐에 남은 프로세스가 없을 때
            count+=1 # 반환 순서 올림
            break # 종료

        if curPri >= maxNum(newPriorities): # 일반 max 함수도 사용 가능
            # 현재 프로세스의 우선순위가 가장 높거나 같을때
            count+=1  # 반환 순서 올림
            if location == curIndex:
                # 목표 프로세스라면 종료
                break

        else:
            # 현재 프로세스의 우선순위보다 높은 프로세스가 우선순위 큐에 있다면
            # 현재 프로세스를 맨 뒤로 보내기
            newPriorities.append(curPri)
            index.append(curIndex)
    return count

def maxNum(array):
    heap = []
    # 최대 힙 활용 : 우선 순위가 높은 것이 먼저 삭제
    for p in array:
        heapq.heappush(heap, -p)
    return -heapq.heappop(heap)

if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2
    # return 1

    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    # return 5

    priorities = [1]
    location = 0
    # return 1

    print(solution(priorities, location))
