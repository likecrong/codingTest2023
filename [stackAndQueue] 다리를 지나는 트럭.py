# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def sumOfBridge(array): # 현재 다리 위 트럭 총 무게
    total = 0
    for node in array:
        total += node[0]
    return total
def solution(bridge_length, weight, truck_weights): # 다리 길이, 다리 최대 무게, 대기 큐
    answer = 0 # 전체 시간
    tw = deque(truck_weights) # 대기 큐
    queue = deque() # 현재 다리 큐

    while True:
        # 1. 퇴장 하기
        if len(queue)>0:
            if queue[0][1]==bridge_length:
                queue.popleft()

        # 2. 트럭별 시간 카운트
        for i in range(len(queue)):
            queue[i][1]+=1

        # 3. 입장 무게 확인
        if len(tw)>0:
            cur = tw[0]
            if (cur+sumOfBridge(queue))<=weight:
                queue.append([tw.popleft(),1])

        # 4. 전체 시간
        answer += 1

        # 5. [예외처리] 모든 큐 종료
        if len(queue) == 0 and len(tw) == 0:
            break
        pass
    return answer

if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    # return 8

    bridge_length = 100
    weight = 100
    truck_weights = [10]
    # return 101

    bridge_length = 100
    weight = 100
    truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # return 110
    print(solution(bridge_length, weight, truck_weights))
