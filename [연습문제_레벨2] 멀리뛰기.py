# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

# 세번째 풀이 : DP 사용
from collections import deque
def solution(n):
    queue = deque([1,2]) # n이 1, 2일 때 값 (DP)
    if n==1:
        return 1%1234567
    elif n==2:
        return 2%1234567
    else: # n이 3 이상일 때
        for index in range(2,n):
            # queue 안에 원소는 반드시 2개 유지
            queue.append(queue[0]+queue[1]) # DP 조건
            queue.popleft() # 계산에 사용된 첫번째 원소 삭제
            #print(queue)
            #print()
        return queue[1]%1234567 # 정답
    pass

if __name__ == '__main__':
    n = 4
    # result 5

    n = 3
    # result 3
    pass

# 첫번째 풀이 : 실패 및 시간초과
'''
from itertools import permutations
from collections import deque
def solution(n):
    listN = deque([1 for x in range(n)])
    sum = 0
    while True:
        print(set(list(permutations(*[listN]))))
        sum += len(set(list(permutations(*[listN]))))
        if len(listN)>2: # 알고리즘 오류
            for i in range(2):
                listN.popleft()
            listN.append(2)
        else:
            break
    return sum # 문제 조건 적용 안함 (정답에 1234567 나눈 나머지)
'''

# 두번째 풀이 : 시간 초과
# 시간을 고려하지 않은 정답
'''
from collections import deque
from itertools import permutations
def solutionAns(n):
    num = deque([2 for x in range(n // 2)])
    if n%2!=0:
        num.append(1)
    #print(num)
    answer = 0
    while True:
        #print(num)
        cur = set(list(permutations(*[num])))
        #print(cur)
        #print(len(cur))
        answer += len(cur)
        node = num.popleft()
        if node==2:
            num.extend([1,1])
        else:
            break
        pass
    return answer%1234567
'''
