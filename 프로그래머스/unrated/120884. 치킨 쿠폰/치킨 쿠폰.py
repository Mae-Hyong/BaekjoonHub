def solution(chicken):
    answer = 0
    while chicken >= 10:
        eaten = chicken // 10
        answer += eaten
        chicken = chicken % 10 + eaten
    return answer