# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    answer = 0 # scovile 지수를 K이상으로 만들기 위한 과정의 수
    heapq.heapify(scoville) # scovile 리스트를 최소 heap으로 전환 (오름차순 정렬)
    while scoville:
        target = heapq.heappop(scoville) # 첫 번째 원소
        if target < K and len(scoville)>=1: # 첫 번째 원소가 K보다 작고, 다음 원소가 heap에 남아 있을 때
            num = target + (2*heapq.heappop(scoville)) # 수식 연산
            heapq.heappush(scoville, num) # 연산 값을 heap에 추가
        elif target < K: # 첫 번째 원소이자 마지막 원소, K보다 작을 때
            # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            answer = -1 # 예외 처리
            break
        else: # 모든 음식의 스코빌 지수가 K 이상일 경우
            break
        answer+=1 # 과정의 수 증가
        pass
    return answer # 과정의 수 반환

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    # return 2

    scoville = [1, 2]
    K = 7
    # return -1

    print(solution(scoville, K))
