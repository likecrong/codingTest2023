# [연습문제_레벨2] 최솟값 만들기.py
# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    A = sorted(A) # 오름차순 정렬
    B = sorted(B,reverse=True) # 내림차순 정렬
    answer = 0 # 연산 후 누적 합 (정답)
    for index in range(len(A)): # 두 리스트는 같은 길이
        answer+=A[index]*B[index] 
        # 현재 가능한 가장 큰 값과 작은 값을 곱해 누적합
        # 이유 : 두 리스트의 연산 후 누적합이 최소값이 되기 위해서
    return answer

if __name__ == '__main__':
    A = [1, 4, 2]
    B = [5, 4, 4]
    # answer 29

    A = [1, 2]
    B = [3, 4]
    # answer 10

    print(solution(A,B))
