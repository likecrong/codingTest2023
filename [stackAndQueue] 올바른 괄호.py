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
        '''
        print('----------')
        print(s)
        print(word)
        print(tmp)
        print('----------')
        '''
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
