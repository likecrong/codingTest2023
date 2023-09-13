# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    length = len(number)
    listNum = list(number)
    answer = ""
    target = length-k-1

    # 첫번째 풀이 : 전체 문자열 리스트 중 자리수를 지정해 탐색
    # 문제점 : 런타임
    '''
    while target>-1:
        #print('현재 남은 자리수', target)
        if target == 0:
            listTarget = listNum[:]
        else:
            listTarget = listNum[:-target]
        #print('검색 리스트', listTarget)
        maxNum = max(listTarget)
        #print('검색 리스트 중 최댓값', maxNum)
        answer += maxNum
        index = listTarget.index(maxNum)
        #print('검색 리스트 중 최댓값 위치', index)
        listNum = listNum[index+1:]
        #print(listNum)
        target-=1
    '''
    # 두번째 풀이 : 첫번째 풀이와 같은 방식을 이용하되, 9일 경우 무조건 answer에 추가
    # 문제점 : 런타임
    while target>-1:
        #print('현재 남은 자리수', target)
        if target == 0:
            listTarget = listNum[:]
        else:
            listTarget = listNum[:-target]
        #print('검색 리스트', listTarget)

        maxIndex = 0
        maxNum = listTarget[maxIndex]
        for index in range(len(listTarget)):
            if listTarget[index] == "9":
                #print("같을때")
                maxNum = "9"
                maxIndex = index
                break
            else:
                if maxNum < listTarget[index]:
                    maxNum = listTarget[index]
                    maxIndex = index

        #print('검색 리스트 중 최댓값', maxNum)
        answer += maxNum
        #print('검색 리스트 중 최댓값 위치', index)
        listNum = listNum[maxIndex+1:]
        #print(listNum)
        target-=1 # 자리수 줄이기
    return answer # 나열된 문자

if __name__ == '__main__':
    number = "1924"
    k = 2
    # return "94"

    number = "1231234"
    k = 3
    # return "3234"
    
    number = "4177252841"
    k = 4
    # return "775841"

    print(solution(number, k))
