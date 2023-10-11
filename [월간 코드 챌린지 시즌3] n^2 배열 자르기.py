# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    arr = [] # 정답 배열
    i = left//n # 왼쪽 값(1차원 기준)을 2차원 배열로 전환했을 때 행
    j = left%n # 왼쪽 값(1차원 기준)을 2차원 배열로 전환했을 때 열
    #print(i)
    #print(j)

    for x in range(right-left+1): # 1차원 배열 기준, 조건에 필요한 원소의 갯수
        # 2차원 배열 기준, 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
        if i>=j:
            arr.append(i+1)
        else:
            arr.append(j+1)

        # 인덱스 설정
        if j == n-1: # 마지막 열 일때
            i += 1 # 다음 행 전환
            j = 0 # 첫번째 열 전환
        else: # 마지막 열이 아닐때
            j+=1 # 다음 열 전환
        pass
    return arr # 정답

if __name__ == '__main__':
    n = 3
    left = 2
    right = 5
    # result [3, 2, 2, 3]

    n = 4
    left = 7
    right = 14
    # result [4, 3, 3, 3, 4, 4, 4, 4]

    print(solution(n, left, right))
