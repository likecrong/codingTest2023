# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    length = len(nums) # 포켓몬의 종류 번호가 담긴 배열의 길이
    target = length//2 # 포켓몬 배열 중 선택할 마리 수
    newNum = set(nums) # 배열 중복 제거
    cur = len(newNum) # 포켓몬 종류 수

    '''
    countSet = {} # 포켓몬 종류별 마리수 셋
    # 포켓몬 종류별 마리수 구하기
    for n in nums:
        if n in countSet: # 셋 안에 키가 존재하면 value 증가
            countSet[n] += 1
        else: # 처음 key를 등록
            countSet[n] = 1
    cur = len(countSet) # 포켓몬 종류 수
    '''
    return cur if target>=cur else target

if __name__ == '__main__':
    nums = [3, 1, 2, 3]
    # result 2

    nums = [3, 3, 3, 2, 2, 4]
    # result 3

    nums = [3, 3, 3, 2, 2, 2]
    # result 2

    nums = [1, 1, 1, 1, 1, 1]
    # result 1

    print(solution(nums))
