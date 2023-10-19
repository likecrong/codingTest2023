# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 설명 : 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 반환
from collections import deque, Counter
def solution(numbers, target): # 입력 리스트, 타겟 숫자
    result = deque() # 현재 인덱스와 연산결과를 저장하는 큐
    numque = deque(numbers) # 입력 리스트 -> 입력 큐
    index = 1 # 현재 인덱스
    while numque: # 입력 큐 모두 탐색하면 종료
        cur = numque.popleft() # 현재 입력 큐의 첫번째 원소 반환
        if len(result) == 0: # 첫번째 조건 연산이라면
            # 현재 인덱스와 첫번째 원소(+,-) 각각 추가
            result.append((index, cur))
            result.append((index, -cur))
        else: # 두번째 ~ n번째 조건 연산이라면
            while result[0][0] == index-1: # (현재 인덱스 -1) 값을 가지는 원소에 대해
                newi, newc = result.popleft() # 반환
                # 현재 인덱스와 첫번째 원소(+,-) 각각 추가
                result.append((index, newc+cur))
                result.append((index, newc-cur))
        index+=1 # 다음 인덱스
        pass
    return Counter(result)[(index-1,target)] # 모든 연산 결과 중 타켓값을 가지는 원소의 개수 반환
if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    # return 5

    numbers = [4, 1, 2, 1]
    target = 4
    # return 2

    print(solution(numbers, target))
