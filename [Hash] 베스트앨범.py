# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = [] # 베스트 앨범에 들어갈 노래의 고유번호 순서 리스트
    musicSet = {} # 장르 기준, 노래별 재생수
    numofPlay = {} # 장르 기준, 해당 노래의 총 재생수
    length = len(genres) # 탐색 노래의 총 개수

    # musicSet, numofPlay 원소 설정
    for i in range(length):
        g = genres[i]
        p = plays[i]
        if g in musicSet: # 해당 장르가 존재하면
            musicSet[g].append((-p,i)) # 최대 재생수가 앞에 정렬되기 위함
            numofPlay[g] += p
        else: # 처음 장르를 저장하면
            musicSet[g] = [(-p,i)] # 최대 재생수가 앞에 정렬되기 위함
            numofPlay[g] = p
    #print(musicSet)
    #print(numofPlay)
    #print()

    while len(numofPlay)>0: # 모든 장르 탐색
        maxGenre = max(numofPlay, key=numofPlay.get) # 총 재생수가 가장 높은 장르
        numofPlay.pop(maxGenre) # 탐색 완료 후 삭제
        target = musicSet[maxGenre] # 노래별 재생수 탐색 시작
        if len(target)==1: # 노래가 1개라면
            answer.append(target[0][1]) # 고유번호 추가
            continue # 다음 장르 탐색 지시
        else:
            target.sort() # 재생수가 높은 순서대로 정렬
            #print(target)
            for i in range(2): # 가장 많이 재생된 노래 2개 선정
                answer.append(target[i][1]) # 고유번호 추가
    return answer

if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    # return [4, 1, 3, 0]

    genres = ["classic", "classic", "classic", "classic"]
    plays = [500, 600, 150, 150]
    # return [1, 0]

    print(solution(genres, plays))
