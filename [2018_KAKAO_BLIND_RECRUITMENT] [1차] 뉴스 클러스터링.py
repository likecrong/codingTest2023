# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/17677
from collections import deque, Counter
def checkASC(word): # 입력 글자가 소문자 영문인지 확인하는 함수
    return True if ord(word) >= 97 and ord(word) <= 122 else False
def twoBlock(string): # 입력 문자열을 두글자씩 끊어서 저장하는 함수
    result = [] # 출력 리스트
    queue = deque(string) # 입력 문자열을 한 개씩 저장하는 큐
    while queue:
        target1 = queue.popleft() # 첫번째 문자
        if len(queue) == 0: # 두번째 문자가 존재하지 않는다면
            break # 종료
        target2 = queue[0] # 두번째 문자
        if checkASC(target1) and checkASC(target2): # 첫번째 문자와 두번째 문자가 소문자 영문이라면
            result.append(target1+target2) # 출력 리스트에 추가
    return result # 출력리스트 반환
def solution(str1, str2): # 두 가지 입력 문자열
    # step1 : 두 입력 문자열을 소문자로 변환해 두글자씩 끊어서 저장
    A = twoBlock(str1.lower())
    B = twoBlock(str2.lower())

    if len(A) == 0 and len(B) == 0: # 두 리스트가 모두 비었다면
        answer = 1 # 자카드 유사도 J(A,B) = 1
    else: # 아니라면
        # step2 : 두 리스트 원소 카운트
        ca = Counter(A)
        cb = Counter(B)

        # step3 : 두 리스트 내 중복 제거
        setCA = set(ca.keys())
        setCB = set(cb.keys())

        # step4 : 교집합 연산
        intersection = setCA & setCB # 교집합 결과
        intersectionNum = 0 # 교집합 결과 내 원소 개수 카운트 변수
        for num in intersection:
            intersectionNum += min(ca[num],cb[num]) # 규칙 : 다중집합 고려한 연산
        #print(intersectionNum)

        # step5 : 합집합 연산
        union = setCA | setCB # 합집합 결과
        unionNum = 0 # 합집합 결과 내 원소 개수 카운트 변수
        for num in union:
            unionNum += max(ca[num], cb[num]) # 규칙 : 다중집합 고려한 연산
        #print(unionNum)

        # step6 : 자카드 유사도 연산
        answer = intersectionNum/unionNum
        #print(answer)

    return int(answer*65536)# 출력조건

if __name__ == '__main__':
    str1 = 'FRANCE'
    str2 = 'french'
    # answer 16384

    str1 = 'handshake'
    str2 = 'shake hands'
    # answer 65536

    str1 = 'aa1+aa2'
    str2 = 'AAAA12'
    # answer 43690

    str1 = 'E=M*C^2'
    str2 = 'e=m*c^2'
    # answer 65536

    print(solution(str1, str2))
