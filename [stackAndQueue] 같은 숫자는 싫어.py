# 문제 링크 : 
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

from collections import deque
def solution(arr):
    arr = deque(arr) # 선입 선출을 위한 자료구조 큐
    answer = [] # 연속적인 숫자를 삭제한 리스트
    answer.append(arr.popleft()) # 첫 번째 원소는 비교하지 않고 answer에 추가
    
    # [예외처리] arr이 빈 상태라면 수행하지 않음
    while arr:
        start = arr.popleft()
        if start == answer[-1]: # 가장 최근 추가된 answer의 원소와 내용이 같다면 연속적인 숫자로 판단
            continue # 넘기기
        answer.append(start)
        #print(arr)
        #print(answer)
        pass
    return answer


if __name__ == '__main__':
    #arr=[1,1,3,3,0,1,1]
    arr=[4,4,4,3,3]
    print(solution(arr))
