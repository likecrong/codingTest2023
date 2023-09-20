# [월간 코드 챌린지 시즌1] 이진 변환 반복하기.py
# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
from collections import Counter
def solution(s):
    count = 0 # 최종 몇번의 이진 변환을 거치는지 저장
    numOfRemove0 = 0 # 최종 제거된 0의 개수를 저장
    while s != '1': # 현재 문자열이 '1'이라면 탈출(최종결과)
        cur = Counter(s) # s(문자열) 안에 '0'과 '1'의 개수 카운트
        numOfRemove0+=cur['0'] # 제거할 0의 개수 누적합
        s = str(bin(cur['1']))[2:] # 0 제거 후 길이 -> 이진수 변환 -> 0b 제거 -> 남은 뒷자리 저장
        #print(s)
        count +=1 # 이진 변환 수 카운트
    return [count, numOfRemove0] # 최종 반환 리스트

if __name__ == '__main__':
    s = "110010101001"
    # result [3, 8]

    s = "01110"
    # result [3, 3]
    
    s = "1111111"
    # result [4, 1]

    print(solution(s))
