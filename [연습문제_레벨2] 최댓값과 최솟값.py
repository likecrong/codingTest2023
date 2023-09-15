# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    result = [int(x) for x in s.split()] 
    # 주어진 문자열을 공백으로 구분해 리스트를 생성한 후, 원소를 int형으로 전환
    return str(min(result))+' '+str(max(result)) #최솟값과 최댓값을 문자열로 전환 후, 공백으로 구분해 반환

if __name__ == '__main__':
    s = "1 2 3 4"
    # return "1 4"

    s = "-1 -2 -3 -4"
    # return "-4 -1"

    s = "-1 -1"
    # return "-1 -1"

    print(solution(s))
