# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque
def solution(s):
    queue = deque(s) # 문자열 s를 왼쪽으로 한칸씩 회전하는 큐
    length = len(queue) # 큐의 길이 저장

    condition = {'{':'}', '(':')', '[':']'} # 대괄호, 중괄호, 소괄호 한쌍
    count = 0 # 문자열 s를 왼쪽으로 한칸씩 회전해 초기 문자열과 같아지면 종료하는 조건 변수
    answer = 0 # 해당 문자열이 올바른 괄로 문자열인지 카운트하는 변수
    while count<length: # 문자열 s를 왼쪽으로 한칸씩 회전해 초기 문자열과 같아지면 종료
        #print('확인 ',queue)
        stack = list(queue.copy()) # 큐를 스택으로 복사 : 현재 확인할 괄호 문자열
        #print(stack)

        i = 0 # 현재 인덱스
        while stack: # 스택이 비면 종료
            if (len(stack)-1)<=i: # 실수 구간 : 스택의 길이가 변하기 때문에 지속적인 확인 필요
                # 현재 인덱스가 스택의 마지막 인덱스와 같거나 클 경우
                # 런타임 에러 주의
                break # 종료
            #print(stack)
            #print(i)
            target = stack[i] # 현재 비교할 괄호
            if target not in condition.keys(): # 닫힌 괄호라면
                break # 종료
            if condition[target] == stack[i+1]:
                # 현재 열린괄호의 짝인 닫힌 괄호와 스택의 다음 인덱스 내용이 같다면
                for x in range(2): # 제거
                    stack.pop(i)
                i = 0 # 현재 인덱스 처음으로 이동
            else:
                i += 1 # 다음 인덱스로 이동
            #print()
            pass
        #print('최종 ',stack)
        if len(stack) == 0: # 현재 괄호 문자열이 올바르다면
            answer+=1 # 정답 추가
        queue.append(queue.popleft()) # 문자열 s를 왼쪽으로 한칸 회전
        count+=1 # 다음
        #print()
        pass
    return answer

if __name__ == '__main__':
    s = "[](){}"
    # result 3

    s = "}]()[{"
    # result 2

    s = "[)(]"
    # result 0

    s = "}}}"
    # result 0
    
    s = "{(["
    # result 0

    s = "{(})"
    # result 0
    
    s = "{{{}"
    # result 0

    print(solution(s))
