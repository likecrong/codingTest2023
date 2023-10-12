# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import deque
def setDict(value, dictionary): # 사전 정의 함수
    if value in dictionary.keys(): # 해당 값이 사전에 존재하면 갯수 증가
        dictionary[value] += 1
    else: # 없다면 해당 값에 대한 원소 추가
        dictionary[value] = 1
    return dictionary # 정의된 사전 반환
def solution(want, number, discount):
    answer = 0 # 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수
    # 실수 : 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜 중 가장 빠른 날이라고 오해

    sig = False # 첫째날 인지 확인하는 변수
    queue = deque(discount) # 전체 할인 제품 큐
    window = deque() # 10 연속 할인 제퓸 큐
    dictOfDiscont = {} # window 내 할인 제품 재고
    dictOfWant = dict(zip(want, number)) # 입력값이 원하는 할인 제품 재고

    while queue: # 전체 할인 제품 확인
        if sig == False: # 첫째날이면
            for x in range(10): # 전체 할인 제품 큐에서 window로 재고 10개 이동
                target = queue.popleft() # 전체 할인 제품 큐에서 첫번째 제품 반환
                window.append(target)  # window에 제품 추가
                dictOfDiscont = setDict(target, dictOfDiscont) # window내 할인 제품 재고 정리
        else: # 첫째날이 아니면
            removeTarget = window.popleft() # 가장 오래된 재고 삭제
            if dictOfDiscont[removeTarget] == 1: # 해당 제품이 1개-> 0개가 된다면
                dictOfDiscont.pop(removeTarget) # 할인 제품 재고 원소 삭제
            else:
                dictOfDiscont[removeTarget] -= 1 # 해당 제품 숫자 감소
            target = queue.popleft() # 전체 할인 제품 큐에서 첫번째 제품 반환
            window.append(target)  # window에 제품 추가
            dictOfDiscont = setDict(target, dictOfDiscont) # window내 할인 제품 재고 정리

        # print('큐', queue)
        # print('윈도우', window)
        # print('원래 재고', dictOfWant)
        # print('현재 재고', dictOfDiscont)
        # print('날짜 ', date)
        # print()

        if dictOfDiscont == dictOfWant: # 원하는 제품들이 모두 할인 가능하다면
            answer += 1 # 정답 추가
        sig = True # 첫째날 -> 다음 날
        pass
    return answer # 정답 반환

if __name__ == '__main__':
    want = ["banana", "apple", "rice", "pork", "pot"]
    number = [3, 2, 2, 2, 1]
    discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
    # result 3
    want = ["apple"]
    number = [10]
    discount = ["banana", "banana", "banana", "banana", "banana",
                "banana", "banana", "banana", "banana", "banana"]
    # result 0
    print(solution(want, number, discount))
