# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def fibo(n):
    dp = [0 for x in range(1000001)] # n이 2이상 100,000 이하
    dp[1] = 1 # F(1)은 1
    for i in range(2,n+1): # 2부터 n까지
        dp[i] = dp[i-1] + dp[i-2] # 피보나치 연산
    return dp[n] # F(n) 반환
def solution(n):
    return fibo(n)%1234567 # 정답 조건

if __name__ == '__main__':
    n = 3
    # return 2

    n = 5
    # return 5

    print(solution(n))
