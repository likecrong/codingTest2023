# 문제 풀이 :
# https://school.programmers.co.kr/learn/courses/30/lessons/131701

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

if __name__ == '__main__':
    elements = [7, 9, 1, 1, 4]
    # result 18

    print(solution(elements))

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
