# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq
from collections import deque

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

def solution(jobs):

    heapq.heapify(jobs)  # 작업 리스트, arrivalTime 기준 오름차순으로 정렬
    length = len(jobs)

    queue = [] # 대기 큐, duration 기준 오름차순으로 정렬
    #heapq.heapify(queue)
    total = [] # 각 작업의 요청부터 종료까지 걸린 시간 리스트

    time = 0

    while True:
        #print("시작")
        #print(jobs)
        #print(queue)
        #print('---------------------------------')
        if len(jobs) == 0 and len(queue) == 0:
            break

        # 1. time 기준, 작업 리스트 -> 대기큐
        count = 0
        for arrival, duraiton in jobs:
            if time >= arrival:
                queue.append([duraiton, arrival])
                #heapq.heappush(queue,[duraiton, arrival])
                count += 1
            else:
                break

        # 2. 작업 리스트 popleft
        for _ in range(count):
            heapq.heappop(jobs)

        # 3. 대기 큐 및 time
        if len(queue)!=0: # 1개 이상의 프로세스가 대기큐에 있다면
            #queue = heapsort(queue) # 소요시간 기준, 오름차순 정렬

            #print(queue)
            queue.sort()
            print(queue)

            # 시간 계산
            tmpTotal = []
            for d,a in queue:
                tmpTotal.append(time-a+d)
            print('tmpTotal ',tmpTotal)

            index = tmpTotal.index(min(tmpTotal))

            #duraiton, arrival = heapq.heappop(queue)
            duraiton, arrival = queue.pop(index)


            time += duraiton
            total.append(time-arrival)

            #print(arrival)
            #print(duraiton)
            #print(time)
            #print('---------------------------------')

        else:
            time += 1

        #print("끝")
        pass
    return sum(total)//length

if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    # 9


    jobs = [[0, 10], [2, 10], [9, 10], [15, 2]]
    # 14

    jobs = [[0, 10], [2, 12], [9, 19], [15, 17]]
    # 25

    jobs = [[0, 1]]
    # 1

    jobs = [[1000, 1000]]
    # 1000

    jobs = [[0, 1], [0, 1], [0, 1]]
    # 2

    jobs = [[0, 3], [1, 9], [2, 6], [30, 3]]
    # 7 틀림 8 나옴
    '''

    jobs = [[0, 10], [4, 10], [15, 2], [5, 11]]
    # 15

    jobs = [[10, 10], [30, 10], [50, 2], [51, 2]]
    # 6

    jobs = [[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]
    # 13

    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # 72 틀림 75 나옴

    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
    # 72 틀림 75 나옴
'''
    print(solution(jobs))

