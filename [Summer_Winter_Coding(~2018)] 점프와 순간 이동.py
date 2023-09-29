# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12980

# 두번째 코드 : 재귀 함수
def solution(n):
    answer = recursion(n)
    return answer
def recursion(n):
    if n == 1: # 현재 탐색 수가 1이면
        return 1 # 1 반환
    if n % 2 == 0:  # 짝수라면
        return recursion(n//2) # 현재 탐색수의 결과값 그대로 반환
    else:  # 홀수라면
        return recursion((n-1)//2)+1 # 현재 탐색수의 결과값 + 1 반환

# 첫번째 코드 : 정확성 테스트 통과, 효율성 테스트 시간 초과
'''
def solution(n):
    dp = [1, 1]
    for i in range(2,n+1):
        if i%2==0: # 짝수
            dp.append(dp[i//2])
        else: # 홀수
            dp.append(dp[i//2]+1)
    #print(dp)
    return dp[n]
'''
if __name__ == '__main__':
    n = 5
    # result 2

    n = 6
    # result 2

    n = 5000
    # result 5

    print(solution(n))
