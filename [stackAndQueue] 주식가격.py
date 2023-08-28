# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque
def solution(prices):
    prices_queue = deque(prices) # 초 단위로 기록된 주식 가격
    answer = [] # 각 주식 가격이 떨어지지 않은 기간

    while prices_queue:
        target = prices_queue.popleft() # 현재 주식 가격
        answer.append(len(prices_queue)) # 한 번도 가격이 떨어지지 않은 경우, 최대 기간으로 설정

        for index, p in enumerate(prices_queue): # 현재 이후, 인덱스(매 초)와 주식 가격
            if target > p: # 만약 현재 주식가격보다 작다면(주식 감소 판단)
                answer[-1] = index+1 # 이후에 검사한 인덱스(초)에 1을 더한 값으로 설정
                break
        '''
        print(target)
        print(prices_queue)
        print(answer)
        print('---------------')
        '''
        pass
    return answer

if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    # return [4, 3, 1, 1, 0]

    prices = [1, 2]
    # return [1, 0]

    print(solution(prices))
