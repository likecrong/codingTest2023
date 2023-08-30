# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from collections import deque
def solution(arr):
    arr = deque(arr)
    answer = []
    answer.append(arr.popleft())
    while arr:
        start = arr.popleft()
        if start == answer[-1]:
            continue
        answer.append(start)
        #print(arr)
        #print(answer)
        pass
    return answer
'''
from collections import deque
'''
def solution(progresses, speeds):
    answer = []
    before = 0 # before 초기값 설정, progresses 내 최대 작업일
    for index, p in enumerate(progresses):
        work = 100-p # 잔여 작업량

        tmp = work//speeds[index] # 최소 작업일 계산

        # after : 현재 progresses의 최소 작업일
        after = tmp if work%speeds[index] == 0 else tmp+1 # [예외처리] 최소 작업일이 하루 더 필요할 경우

        print('----------------')
        print(before)
        print(after)
        print(answer)
        print('----------------')

        if before>=after:
            answer[-1]+=1
            # 최대 작업일에 못 미칠 경우 기능수 추가

        else:
            before = after
            # 최대 작업일을 현재 최소 작업일로 변경
            answer.append(1)
            # 작업 분리후, 기능 수 카운트 초기화
    return answer
'''

'''
if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    # return = [2, 1]

    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    # return = [1, 3, 2]

    progresses = [55, 60, 65]
    speeds = [5, 10, 7]
    # return = [3]
    print(solution(progresses, speeds))
'''
'''
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    #arr=[1,1,3,3,0,1,1]
    #arr=[4,4,4,3,3]
    #print(solution(arr))

    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    # return = [2, 1]

    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    # return = [1, 3, 2]

    progresses = [55, 60, 65]
    speeds = [5, 10, 7]
    # return = [3]
    print(solution(progresses, speeds))
'''
'''
# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12909
from collections import deque
def solution(s):

    tmp = deque() # 열린 괄호를 보관하는 큐
    s = deque(s) # 전체 문장을 보관하는 큐

    while s:
        word = s.popleft()
        if word == ")": # 닫힐 괄호를 마주하면
            if len(tmp) != 0:
                tmp.pop() # 열린 괄호 보관 큐에서 가장 최근 괄호 버리기
            else: # 버릴 괄호가 없다면
                return False
        else: # 열린 괄호를 마주하면
            tmp.append("(") # 열린 괄호 보관 큐에 추가
        print('----------')
        print(s)
        print(word)
        print(tmp)
        print('----------')
        pass
    # 열린 괄호 보관 큐에 아무 것도 없다면 True 반환
    return True if len(tmp) == 0 else False
    
if __name__ == '__main__':
    s = "()()"
    # true
    s = "(())()"
    # true
    s = ")()("
    # false
    s = "(()("
    #false
    print(solution(s))

'''
'''
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
'''
'''
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

'''
'''
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
        
        print(target)
        print(prices_queue)
        print(answer)
        print('---------------')
        
        pass
    return answer

if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    # return [4, 3, 1, 1, 0]

    prices = [1, 2]
    # return [1, 0]

    print(solution(prices))
        
'''
'''
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
'''
import heapq



def solution(jobs):
    length = len(jobs)
    heapq.heapify(jobs)
    queue = []
    heapq.heapify(queue)
    print('jobs : ',jobs)

    sum = 0
    time = 0
    # 2. 비교
    while True:
        print('jobs : ', jobs)

        testLength = len(jobs)
        for index in range(testLength):
            if time > jobs[index][0]:  # 요청시간이 현재시간보다 앞서면
                heapq.heappush(queue, [jobs[index][1], jobs[index][0]])  # 소요시간, 요청시간
            else:
                print('큐는 존재, 시간이 초과')
                time+=1
                index-=1
                break

        for i in range(index):
            heapq.heappop(jobs)

        if len(queue)!=0:
            # 요청시간에 상관없이 소요시간이 작은 순으로 정렬
            print('queue : ', queue)
            target = heapq.heappop(queue)
            print('-------------------------')
            print('target : ', target)
            print(target[0])
            print(target[1])
            print(time)

            print('-------------------------')


            print(target[0]+time-target[1])
            sum+=(target[0]+time-target[1])
            print('sum : ', sum)
            print('time : ', time)

            time+=target[0]
        pass
    return sum//length



if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    # return 9
    '''
    jobs = [[0, 3], [10, 1]]
    # return 2

    jobs = [[7, 8], [3, 5], [9, 6]]
    # return 9
    
    jobs = [[0, 5], [2, 10], [10000, 2]]
    #return 6
    
    jobs = [[1, 4], [7, 9], [1000, 3]]
    # return 5

    
    jobs = [[0, 1], [2, 2], [2, 3]]
    # return 2
    
    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # return 72
    
    jobs = [[0, 5], [2, 10], [10000, 2]]
    # return 6
    '''
    print(solution(jobs))

