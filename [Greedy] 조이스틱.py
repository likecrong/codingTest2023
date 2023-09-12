# 문제 링크 :
# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 65~90 : 대믄지 알파벳
# 97~122 : 소문자 알파벳
def solution(name):
    # 첫번째 풀이 : 미리 알페벳 이동이 작은 것을 계산해놓고,
    # 커서를 왼쪽, 오른쪽 한 방향으로만 이동하는 것 중 최소값 찾기 -> 오류 발생
    listOfName = list(name)
    length = len(listOfName)
    cur = []
    weight = []

    for index in range(length):
        cur.append("A")
        # 다음 알파벳
        up = ord(listOfName[index]) - ord(cur[index])
        # 이전 알파벳
        down = 91 - ord(listOfName[index])
        if up > down:
            weight.append(down)
        else:
            weight.append(up)
    #print(cur)
    #print(weight)

    left = 0
    index = 0
    tmp = cur[:]
    while True:
        left += weight[index]
        tmp[index] = listOfName[index]
        #print('left ', left)
        #print(tmp)
        #print(index)
        #print('000000000000000000000000000000')
        if tmp == listOfName:
            #print("종료")
            break
        if index == 0:
            index = length-1
        else:
            index -= 1
        left+=1
    #print(left)

    index = 0
    tmp = cur[:]
    right = 0
    #print(tmp)
    while True:
        right += weight[index]
        tmp[index] = listOfName[index]
        #print('right ', right)
        #print(tmp)
        #print(index)
        #print('000000000000000000000000000000')
        if tmp == listOfName:
            break
        if index == length-1:
            index = 0
        else:
            index += 1
        right+=1
    #print(right)

    return right if left>right else left

if __name__ == '__main__':
    name = "JAZ"
    # return 11
    name = "JEROEN"
    # return 56
    name = "JAN"
    # return 23

    # 예외 발견 : 한 방향으로만 해결하면 안된다.
    name = "ABAAAAAAAAABB"

    print(solution(name))
