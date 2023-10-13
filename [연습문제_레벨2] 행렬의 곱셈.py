# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

from collections import deque
def solution(arr1, arr2):
    answer = [] # 두 2차원 행렬을 곱한 결과
    queue = deque(arr1) # 왼쪽 행렬 리스트를 큐로 전환

    # step1 : 오른쪽 행렬을 열별로 재배치 하기
    # ex) [[1,2],[3,4]] -> [[1,3],[2,4]]
    length = len(arr2[0]) # 오른쪽 행렬의 열의 개수 저장
    newArr = [[] for _ in range(length)] # 해당 길이에 맞춰 빈 이중 리스트 생성
    for node in arr2: # 오른쪽 행렬에 대해
        for i in range(length): # 각 열에 대해
            newArr[i].append(node[i]) # 변환
    #print(newArr)

    # step2 : 재배치한 행렬과 왼쪽 행렬의 각 원소를 곱하기
    while queue: # 왼쪽 행렬의 모든 원소를 연산하면 종료
        left = queue.popleft() # 왼쪽 행렬의 원소 1개씩 반환
        tmp = [] # 연산 결과를 저장할 임시 리스트
        for right in newArr: # 오른쪽 행렬의 원소 1개씩 반환
            result = 0 # 연산 결과를 저장할 리스트
            for i in range(len(right)): # 오른쪽 행렬의 열에 대해
                result += left[i]*right[i] # 연산
            tmp.append(result) # 연산 종료 후 임시 리스트에 추가
        answer.append(tmp) # 임시 리스트를 정답 리스트에 추가
        pass
    return answer # 반환

if __name__ == '__main__':
    arr1 = [[1, 4], [3, 2], [4, 1]]
    arr2 = [[3, 3], [3, 3]]
    # return [[15, 15], [15, 15], [15, 15]]

    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    # return [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

    print(solution(arr1, arr2))
