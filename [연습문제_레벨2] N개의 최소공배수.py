# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12953
def solution(arr):
    maxNum = max(arr) # 문제 배열의 최대값
    target = maxNum # 다른 숫자 원소들과 비교할 대상
    index = 1 # 곱셈 연산을 위한 인덱스

    arr.remove(maxNum) # 문제 배열에서 최대값 삭제
    # 이유 : 비교 연산에서 제외하기 위해
    
    while True:
        count = 0 # target에 대해 모든 원소들이 조건에 만족하는지 확인하는 변수
        for num in arr: # 모든 원소들에 대해
            if target%num==0: # 최소 공배수 조건
                count += 1 # 조건 만족 확인
            else: # 한 개의 원소라도 조건에 만족하지 않는 다면
                break # 종료
        if count == len(arr): # 모든 원소가 최소 공배수 조건에 만족하면
            return target # 최소 공배수 반환
        else: # 만족하지 않는다면
            # 최대값 * (2,3,4 ...) 을 비교 대상으로 설정
            index += 1 
            target = maxNum * index
        pass
    pass

if __name__ == '__main__':
    arr = [2, 6, 8, 14]
    # result 168

    arr = [3, 2, 1]
    # result 6

    print(solution(arr))
