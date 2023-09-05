# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter
def solution(participant, completion):
    countP = Counter(participant) # 참가자 명단 내 이름별 갯수
    countC = Counter(completion) # 완주자 명단 내 이름별 갯수
    return list((countP-countC).items())[0][0] # 각 카운터의 차집합 중 단일한 이름을 반환

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    # return "leo"

    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    # return "vinko"
    
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    # return "mislav"

    print(solution(participant, completion))
