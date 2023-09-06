# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    phone_book.sort() # 접두어를 비교해야 하기 때문에 오름차순 정렬
    length = len(phone_book) # 전화번호부 길이

    # 전화번호부의 원소들이 각각 접두어가 되어 다른 번호에 포함되는 지 확인
    for index in range(length-1):
        target=phone_book[index]
        if phone_book[index + 1].startswith(target): # 포함 된다면
            return False
    return True # 한 개도 포함되지 않는다면


if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]
    # return false

    phone_book = ["123", "456", "789"]
    # return true

    phone_book = ["12", "123", "1235", "567", "88"]
    # return false

    print(solution(phone_book))
