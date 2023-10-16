# 문제 링크 : 
# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque
def solution(cacheSize, cities):
    queue = deque(cities) # input 큐
    window = deque() # 지정된 캐시크기를 가지는 window 큐
    answer = 0 # 실행 시간

    while queue: # input 큐의 모든 내용을 처리하면 종료
        # print('처음')
        # print(queue)
        # print(window)
        # print()
        target = queue.popleft() # 현재 도시 이름 반환
        target = target.lower() # 현재 도시 이름을 소문자로 변경(일원화)
        if target not in window: # window에 현재 도시 이름이 없다면
            answer += 5 # cache miss
        else: # window에 현재 도시 이름이 있다면
            window.remove(target) # 삭제
            answer += 1 # cache hit
        window.appendleft(target) # 현재 도시 이름을 가장 최근 위치에 저장(가장 왼쪽)
        if len(window) > cacheSize: # 현재 window가 cache size를 벗어난다면
            window.pop() # 가장 오래된 위치에 있는 도시이름 삭제(가장 오른쪽)
        # print('끝')
        # print(queue)
        # print(window)
        # print(answer)
        # print('..........')
        # print()
        pass
    return answer # 실행시간 반환
if __name__ == '__main__':
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    # return 50

    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    # return  21

    cacheSize = 2
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    # return  60

    cacheSize = 5
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    # return  52

    cacheSize = 2
    cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
    # return  16
    
    cacheSize = 0
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    # return  25
    
    print(solution(cacheSize, cities))
