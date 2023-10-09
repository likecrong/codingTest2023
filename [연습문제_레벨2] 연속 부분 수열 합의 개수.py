# 문제 풀이 :
# https://school.programmers.co.kr/learn/courses/30/lessons/131701

# 세번째 풀이 : 성공
# 이유 : 입력 배열의 sort 적용 해제 -> 문제 오해 (자료 그림에 속지 말기)
from collections import deque
def solution(elements):
    # elements.sort() # 실패 원인
    queue = deque(elements) # 큐 자료구조 사용
    length = len(queue) # 입력 배열 길이
    result = [] # 원형 수열 내 모든 부분수열의 합 저장
    totalLoop = 0 # 입력 배열 원소에 대해 1번씩 연산을 수행하기 위한 조건 변수
    
    while length>totalLoop: # 입력 배열의 길이만큼 반복
        target = queue.popleft() # 현재 입력 배열의 첫번재 원소 탈출
        count = target # 부분수열의 합 연산 변수 (길이가 2일때, 초기값 지정)
        for num in queue: # 길이가 2부터 n까지
            count += num # 부분수열의 합 연산
            result.append(count) # 저장
        queue.append(target) # 첫번째 원소를 마지막 원소로 삽입
        totalLoop += 1 # 다음 입력 배열 원소 이동
        #print(result)
        pass
    result.extend(queue) # 길이가 1일때, 부분수열의 합 삽입
    #print(result)
    return len(set(result)) # 전체 합 리스트에서 중복을 제외한 갯수 반환

# 첫번째 풀이 : 실패
'''
def solution(elements):
    sortElements = sorted(elements)
    #print(sortElements)
    length = len(sortElements)

    numList = []
    for n in range(1, length+1): # 길이
        for index in range(length):
            target = index+n
            #print(target)
            if target <= length:
                #print(sortElements[index:target])
                numList.append(sum(sortElements[index:target]))
            else:
                tmp = sortElements[index:]
                tmplength = len(tmp)
                num = n-tmplength
                #print('현재 ',num)
                #print(tmp+sortElements[:num])
                numList.append(sum(sortElements[index:]+sortElements[:num]))
            #print(numList)
            #print()
    return len(set(numList))
'''
'''
# 두번째 풀이 : 실패 및 시간초과
from collections import deque
def solution(elements):
    queue = deque(sorted(elements))
    length = len(queue)
    numList = []
    for i in range(1,length+1):
        #print(i)
        for index in range(1, length + 1):
            sum = 0
            #print(queue)
            for num in range(i):
                #print(num)
                node = queue.popleft()
                sum+=node
                queue.append(node)
            #print(queue)
            numList.append(sum)
        #print(numList)
        #print()
    return len(set(numList))
'''
if __name__ == '__main__':
    elements = [7, 9, 1, 1, 4]
    # result 18

    print(solution(elements))
