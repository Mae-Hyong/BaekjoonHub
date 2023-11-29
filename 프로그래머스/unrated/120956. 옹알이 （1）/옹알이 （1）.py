def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        for j in speak:
            i = i.replace(j, ' ')
        i = i.replace(' ', '')
        if len(i) == 0:
            answer += 1
    return answer