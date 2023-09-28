# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    length = len(words) # 단어 리스트의 길이
    queue = [] # 이미 조사한 단어 리스트
    sig = False # 탈출 조건에 의한 탈출 여부
    for index in range(1,length):
        cur = words[index] # 2번째 단어부터
        pre = words[index-1] # 1번째 단어부터
        #print(cur)
        #print(pre)
        #print()
        if cur[0] != pre[-1]: # 현재 단어의 시작과 이전 단어의 끝이 다르다면
            sig = True # 설정
            break # 종료
        queue.append(pre) # 이전 단어를 조사한 단어 리스트에 추가
        if cur in queue: # 현재 단어가 이미 조사한 단어 리스트에 있다면 (중복)
            sig = True # 설정
            break # 종료
        pass

    # 반환 : [가장 먼저 탈락하는 사람의 번호, 그 사람이 몇번째 턴에서 탈락하는 지]
    # 두 탈락 조건 중 1개라도 해당 되지 않는 다면 [0,0] 반환
    return [index%n+1,index//n+1] if sig==True else [0,0]

if __name__ == '__main__':

    # 중복일 때
    n = 3
    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    # result [3, 3]

    # 지는 사람이 없을 때
    n = 5
    words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    # result [0, 0]
    
    # 단어의 끝과 시작이 연결되지 않을 때
    n = 2
    words = ["hello", "one", "even", "never", "now", "world", "draw"]
    # result [1, 3]

    print(solution(n, words))
