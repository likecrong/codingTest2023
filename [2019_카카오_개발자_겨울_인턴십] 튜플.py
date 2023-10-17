# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/64065
from collections import deque
def setDict(dictionary, key): # 해당 키에 대한 빈도수를 저장하는 사전을 설정하는 함수
    if key in dictionary.keys(): # 키가 존재한다면
        dictionary[key] += 1 # 빈도수 증가
    else: # 키가 존재하지 않는다면
        dictionary[key] = 1 # 키와 함께 빈도 수 1 설정
    return dictionary # 연산된 사전 반환
def solution(s):
    # step1 : 해당 문자열에서 가장 왼쪽, 오른쪽 괄호 제거
    s = s[1:]
    s = s[:-1]

    # step2 : 문자열 내 숫자 원소 파악 후, 사전에 해당 숫자 원소의 빈도수 저장
    answerDic = {} # 빈도수 저장 사전
    queue = deque(s) # 문자열을 큐로 저장
    while queue:
        target = queue.popleft() # 가장 왼쪽 문자 반환
        if target == '{': # 열린 괄호라면
            num = '' # 숫자 원소 저장 변수 초기화
        elif target == '}': # 닫힌 괄호라면
            answerDic = setDict(answerDic, int(num)) # 숫자 원소에 대한 빈도수 연산
            if len(queue)>0: # } 다음은 ','이기 때문에
                queue.popleft() # ',' 제거
        elif target == ',': # 숫자 원소와의 구분이라면
            answerDic = setDict(answerDic, int(num)) # 숫자 원소에 대한 빈도수 연산
            num = '' # 숫자 원소 저장 변수 초기화
            # 다음 문자가 숫자이기 때문
        else:
            num += target # 숫자 원소 문자열 추가
        pass

    # step3 : answerDic에서 빈도수를 내림차순 기준으로 정렬
    # ex) return [(100, 3), (1, 2), (50, 1)]
    sorted_dict = sorted(answerDic.items(), key=lambda item: item[1], reverse=True)

    # step4 : 빈도수 내림차순 리스트에서 key값만 뽑아 나열한 리스트 반환
    return [node[0] for node in sorted_dict]

if __name__ == '__main__':
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    # result [2, 1, 3, 4]

    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    # result [2, 1, 3, 4]

    s = "{{20,111},{111}}"
    # result [111, 20]

    s = "{{123}}"
    # result [123]

    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    # result [3, 2, 4, 1]

    print(solution(s))
