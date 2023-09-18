# 2023.09.18
# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/12951
#'''
# 두번째 방법 : 문자열의 문자 하나씩 조사
def solution(s):
    wordlist = list(s) # 한글자씩 문자열 원소로 저장
    #print(wordlist)
    answer='' # JadenCase 적용한 문자열(정답 문자열)
    for w in wordlist: # w(한글자)
        #print(w)
        #print(answer)
        #print()
        if w==' ': # 공백 문자라면
            answer+=w # 정답 문자열에 추가
        else: # 공백 문자가 아니라면
            if len(answer)==0 or answer[-1] == ' ': 
                # 첫번째 문자이거나, 가장 최근에 추가한 문자가 공백 문자라면
                # 이유 : 공백 문자 뒤에는 알파벳 또는 숫자가 있다고 예상
                answer += w.upper() # 대문자로 전환해 정답 문자열에 추가
            else:
                answer += w.lower() # 소문자로 전환해 정답 문자열에 추가
    return answer # 정답 문자열 반환
#'''
'''
# 첫번째 방법 : split 활용
# 문제점 : 공백 문자가 여러개 일때 예외처리 불가
def solution(s):
    wordList = s.split()
    answer = ''
    for word in wordList:
        if len(word)==1:
            answer+=(word[0].upper()+' ')
        else:
            answer += (word[0].upper() + word[1:].lower() + ' ')
    return answer[:-1]
'''
if __name__ == '__main__':
    s = "3people unFollowed me"
    # return "3people Unfollowed Me"

    s = "for the last week"
    # return "For The Last Week"

    s = "3people     unFollowed m"
    # return "3people Unfollowed M"
    
    print(solution(s))
