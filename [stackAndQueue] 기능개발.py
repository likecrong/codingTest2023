# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    before = 0 # before 초기값 설정, progresses 내 최대 작업일
    for index, p in enumerate(progresses):
        work = 100-p # 잔여 작업량

        tmp = work//speeds[index] # 최소 작업일 계산

        # after : 현재 progresses의 최소 작업일
        after = tmp if work%speeds[index] == 0 else tmp+1 # [예외처리] 최소 작업일이 하루 더 필요할 경우

        '''
        print('----------------')
        print(before)
        print(after)
        print(answer)
        print('----------------')
        '''

        if before>=after:
            answer[-1]+=1
            # 최대 작업일에 못 미칠 경우 기능수 추가

        else:
            before = after
            # 최대 작업일을 현재 최소 작업일로 변경
            answer.append(1)
            # 작업 분리후, 기능 수 카운트 초기화
    return answer

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
