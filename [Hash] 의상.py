# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from itertools import combinations, product

def solution(clothes):
    clothesSet = {} # 옷의 카테고리 별 현황 SET
    for c in clothes:
        if c[1] in clothesSet:
            clothesSet[c[1]].append(c[0])
        else:
            clothesSet[c[1]] = [c[0]]
    #print(clothesSet)

    clothesList = list(clothesSet.values()) # 카테고리 이름을 제외한 value 리스트
    #print(clothesList) # [['yellow_hat', 'green_turban'], ['blue_sunglasses']]
    #print(*clothesList) # ['yellow_hat', 'green_turban'] ['blue_sunglasses']
    # 참고 : https://velog.io/@davkim1030/Python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-product-itertools

    '''
    # 첫번째 풀이 : 조합과 데카르트 곱을 사용하여 전체 경우를 계산
    # 문제점 : 시간 초과
    answer = 0 # 계산한 경우의 수
    length = len(clothesSet) # 옷의 카테고리 수
    order = [x for x in range(length)] # 카테고리를 '인덱스화'한 리스트
    #print(order)

    for i in range(1, len(order) + 1):
        target = list(combinations(order, i)) # 카테고리 조합 경우의 수
        for node in target: # 카테고리 경우에 따라 리스트 재조합
            #print(node)
            tmp = [] # 재조합된 리스트
            for index in node:
                #print(index)
                tmp.append(clothesList[index])
            #print(tmp)
            product_list = list(product(*tmp)) #재조합된 리스트로 데카르트 곱 연산
            #print(product_list)
            answer += len(product_list) #해당 값을 계산한 경우의 수에 더함
    
    return answer
    '''
    # 두번째 풀이 : 전체 경우의 수에서 모든 옷을 입지 않은 경우를 빼기
    answer = 1  # 계산한 경우의 수
    for node in clothesList:
        answer *= (len(node)+1) # 해당 카테고리에서 안 입은 경우 (+1) 추가
    return answer -1
if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    # return 5

    clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    # return 3

    print(solution(clothes))
