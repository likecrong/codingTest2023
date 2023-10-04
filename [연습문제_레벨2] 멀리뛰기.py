# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

# 첫번째 풀이 : 실패 및 시간초과
from itertools import permutations
from collections import deque
def solution(n):
    listN = deque([1 for x in range(n)])
    sum = 0
    while True:
        sum += len(set(list(permutations(*[listN]))))
        if len(listN)>2:
            for i in range(2):
                listN.popleft()
            listN.append(2)
        else:
            break
    return sum

if __name__ == '__main__':
    n = 4
    # result 5

    n = 3
    # result 3

    print(solution(n))
