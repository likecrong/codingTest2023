# 문제 링크 : 
# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    queue = list(s) # 문자열 s를 리스트로 저장
    tmp = [] # 임시 배열 (Stack)
    for x in queue: # 리스트 원소를 1번씩만 접근 : O(N)
        #print(x)
        #print(tmp)
        #print()
        if len(tmp)!=0 and x == tmp[-1]:
            # 임시 배열에 원소가 있고, 현재 원소가 임시 배열의 마지막 원소와 같을때
            tmp.pop() # 임시 배열의 마지막 원소 삭제 : 가장 최근 값부터 처리 가능
        else: # 문자열이 연속되지 않을때
            tmp.append(x) # 임시 배열에 추가
    #print(queue)
    #print(tmp)
    return 1 if len(tmp)==0 else 0 # 모든 원소가 짝지어 제거 가능하면 1 반환
if __name__ == '__main__':
    s = 'baabaa'
    # result 1

    s = 'cdcd'
    # result 0

    s = 'c'
    # result 0

    print(solution(s))
  
# 첫번째 시도 : 인덱스 활용 
# 시간 초과, 런타임 에러
'''
def solution(s):
    queue = list(s)
    length = len(queue)
    index = 0

    if length == 1:
        return 0
    while (length-1) > index:
        print('quque ',queue)
        print('index ', index)
        if len(queue) == 0:
            return 1
        print('cur ', queue[index])
        print('next ',queue[index+1])
        print()
        if queue[index] == queue[index+1]:
            queue = queue[:index] + queue[index+2:]
            index = 0
            continue
        index += 1
    return 0
'''
# 두번째 시도 : deque 활용
# 시간 초과, 실패
'''
from collections import deque
def solution(s):
    queue = deque(s)
    wait = deque()

    if len(queue) == 1:
        return 0
    while queue:
        #print(queue)
        #print(wait)
        cur = queue.popleft()
        #print('cur ',cur)
        if len(queue) == 0:
            break
        next = queue[0]
        #print('next ', next)
        #print()
        if cur == next:
            queue.popleft()
            while wait:
                queue.appendleft(wait.pop())
        else:
            wait.append(cur)
    return 1 if len(wait)==0 else 0
'''
# 세번째 시도 : counter 활용
# 시간 초과
'''
from collections import deque, Counter
def countNum(q):
    count = Counter(q)
    value = count.values()
    for v in value:
        if v%2!=0:
            return False
    return True
def solution(s):
    queue = deque(s)
    wait = deque()

    if countNum(queue) == False:
        return 0

    while queue and countNum(queue+wait)==True:
        #print(queue)
        #print(wait)
        cur = queue.popleft()
        #print('cur ',cur)
        if len(queue) == 0:
            break
        next = queue[0]
        #print('next ', next)
        #print()
        if cur == next:
            queue.popleft()
            while wait:
                queue.appendleft(wait.pop())
        else:
            wait.append(cur)
    return 1 if len(wait)==0 else 0
'''
# 네번째 시도 : Stack 활용 
# 시간 초과
'''
from collections import Counter
def countNum(mylist):
    count = Counter(mylist)
    value = count.values()
    for v in value:
        if v%2!=0:
            return False
    return True
def isEqual(x):
    return len(set(x)) <= 1
def solution(s):
    stack = list(s)
    wait = []

    if countNum(stack) == False:
        return 0
    
    while stack and countNum(stack+wait) == True:

        if isEqual(stack + wait):
            return 1

        #print(stack)
        #print(wait)
        cur = stack.pop()
        #print(cur)
        if len(stack) == 0:
            break
        pre = stack[-1]
        #print(pre)
        #print()
        if cur == pre:
            stack.pop()
            stack.extend(wait)
            wait = []
            continue
        wait.append(cur)
    return 1 if len(wait) == 0 else 0
'''
