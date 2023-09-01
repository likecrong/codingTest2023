# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

from collections import deque
def solution(jobs):

    time = []
    length = len(jobs)

    # 1. 시작시간, 종료시간 + 요청시간, 소요시간
    newJobs = []
    for a, d in jobs:
        newJobs.append([a, d, a, d])
    queue = deque(newJobs)

    while queue:
        # 2. 요청 시간 순서로 정렬
        #print(queue)
        queue = sorted(queue)
        print(queue)

        # 3. 가장 첫번째 프로세스(target)의 종료시간과 나머지 프로세스의 시작시간 비교
        # 나머지 프로세스의 시작시간 중에서 target의 종료 시간 이내에 들어오는 원소는
        # 시작시간, 종료시간 update
        target = queue.pop(0)
        print(target)
        time.append(target[1]+target[2]-target[3])

        for index, process in enumerate(queue):
            #print('1번 : ', target[1])
            if target[1] >= process[0]:
                queue[index][0] = target[1]
                queue[index][1] = target[1] + queue[index][3]
        print('--------------------------')

    print(time)
    return sum(time)//length

if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    # 9
    '''
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
    # 7


    jobs = [[0, 10], [4, 10], [15, 2], [5, 11]]
    # 15

    jobs = [[10, 10], [30, 10], [50, 2], [51, 2]]
    # 6

    jobs = [[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]
    # 13
    
    jobs = [[0, 10], [2,10], [9,10], [15,2]]

    jobs = [[0, 10], [2,10], [25,10], [25,2]]

    
    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # 72 틀림 75 나옴
    
    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
    # 72 틀림 75 나옴
'''
    print(solution(jobs))
