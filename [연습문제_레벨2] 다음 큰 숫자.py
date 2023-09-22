# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12911
from collections import Counter
def solution(n):
    countOfN = Counter(bin(n)[2:]) # 주어진 n을 이진수로 변환한 변수
    num = countOfN['1'] # 해당 이진수 중 1의 개수 카운트

    while True:
        n+=1 # 첫째, 주어진 n보다 무조건 큰 자연수
        countOfTarget = Counter(bin(n)[2:]) # 해당 자연수를 이진수로 변환한 변수
        if num == countOfTarget['1']: # 둘째, 주어진 자연수와 해당 자연수의 1의 개수가 같은지 확인
            break # 종료
        pass
    return n # 셋째, 첫째와 둘째 조건을 만족하는 가장 작은 자연수 반환

if __name__ == '__main__':
    n = 78
    # result 83

    n = 15
    # result 23

    print(solution(n))
