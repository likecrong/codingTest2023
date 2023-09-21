# 문제 링크:
# https://school.programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    target = 1 # 자연수 1부터 n//2까지 한개씩 연산하는 변수
    answer = 0 # 연산 후 sum이 n과 같을 때 count 하는 변수 (정답)
    while target <= (n//2): # n의 절반 크기까지 검사 : 더 큰 수는 sum이 n과 같을 수 없음
        num = target # 현재 target의 최솟값
        sum = 0 # 모든 수의 덧셈을 저장하는 변수
        while True:
            #print('num ', num)
            if sum > n: # n보다 합이 크면 실패
                #print('sum ',sum)
                break
            elif sum == n: # 성공
                #print('sum ', sum)
                answer += 1 # 정답 count 추가
                #print('answer ', answer)
                break
            else: # 덧셈 연산
                sum += num # 연속되는 수 덧셈
                num += 1 # 다음 연속 수 설정
            pass
        target += 1 # 최솟값 1 증가
        #print()
    return answer+1 # 본인 자신 1을 추가한 정답 반환

if __name__ == '__main__':
    n =15
    # result 4
    print(solution(n))
