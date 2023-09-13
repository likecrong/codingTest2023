# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42883
from collections import deque
def solution(number, k):
    length = len(number) # 전체 문자열의 길이
    waitQueue = deque(list(number)) # [대기 큐]전체 문자열의 문자를 각각 deque의 원소로 저장
    searchQueue = deque() # 검색 큐
    answer = "" # 가장 큰 숫자 문자열
    target = length-k-1 # 현재 남긴 자리수

    # 세번째 풀이 : LIST 슬라이싱의 시간 복잡도가 O(n)이기 때문에 시간 초과 예상
    # deque를 활용해 시간 복잡도를 줄임
    while target > -1: # 남긴 자리수가 0자리 까지 수행
        #print('현재 남은 자리수', target)
        if target == 0: # 남긴 자리수가 0이면 대기큐 원소 큐를 모두 검색 큐에 전달
            searchQueue.extend(waitQueue)
        else:
            now = len(waitQueue) # 현재 대기 큐의 길이
            searchQueue.extend([waitQueue.popleft() for _ in range(now-target)])
            # 현재 남긴 자리수를 제외한 모든 앞 원소들을 검색 큐에 전달
        #print('검색 큐', searchQueue)

        maxIndex = 0 # 최대값 인덱스
        maxNum = searchQueue[maxIndex] # 최대값
        for index in range(len(searchQueue)):
            if searchQueue[index] == "9": # 현재 원소가 9이면 무조건 최대값
                maxNum = "9"
                maxIndex = index
                break # 종료(시간 단축)
            else: # 현재 최대값과 현 원소 비교
                if maxNum < searchQueue[index]:
                    maxNum = searchQueue[index]
                    maxIndex = index
        #print('검색 큐 중 최댓값', maxNum)
        answer += maxNum # 문자열 추가
        #print('검색 큐 중 최댓값 위치', maxIndex)
        for _ in range(maxIndex+1): # 최대값 원소까지 검색 큐 popleft
            searchQueue.popleft()
        #print(waitQueue)
        target -= 1  # 자리수 줄이기
    return answer  # 나열된 문자

'''
def solution(number, k):
    length = len(number)
    listNum = list(number)

    answer = ""
    target = length - k - 1

    # 첫번째 풀이 : 전체 문자열 리스트 중 자리수를 지정해 탐색
    # 문제점 : 런타임
    
    while target>-1:
        #print('현재 남은 자리수', target)
        if target == 0:
            listTarget = listNum[:]
        else:
            listTarget = listNum[:-target]
        #print('검색 리스트', listTarget)
        maxNum = max(listTarget)
        #print('검색 리스트 중 최댓값', maxNum)
        answer += maxNum
        index = listTarget.index(maxNum)
        #print('검색 리스트 중 최댓값 위치', index)
        listNum = listNum[index+1:]
        #print(listNum)
        target-=1
    
    # 두번째 풀이 : 첫번째 풀이와 같은 방식을 이용하되, 9일 경우 무조건 answer에 추가
    # 문제점 : 런타임
    
    while target>-1:
        #print('현재 남은 자리수', target)
        if target == 0:
            listTarget = listNum[:]
        else:
            listTarget = listNum[:-target]
        #print('검색 리스트', listTarget)

        maxIndex = 0
        maxNum = listTarget[maxIndex]
        for index in range(len(listTarget)):
            if listTarget[index] == "9":
                #print("같을때")
                maxNum = "9"
                maxIndex = index
                break
            else:
                if maxNum < listTarget[index]:
                    maxNum = listTarget[index]
                    maxIndex = index

        #print('검색 리스트 중 최댓값', maxNum)
        answer += maxNum
        #print('검색 리스트 중 최댓값 위치', index)
        listNum = listNum[maxIndex+1:]
        #print(listNum)
        target-=1 # 자리수 줄이기
    
    return answer  # 나열된 문자
'''
if __name__ == '__main__':
    number = "1924"
    k = 2
    # return "94"

    number = "1231234"
    k = 3
    # return "3234"
    
    number = "4177252841"
    k = 4
    # return "775841"

    print(solution(number, k))
