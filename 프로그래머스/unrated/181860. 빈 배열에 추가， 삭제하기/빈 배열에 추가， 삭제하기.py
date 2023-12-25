def solution(arr, flag):
    answer = []
    for i, j in zip(arr, flag):
        if j == False:
            for x in range(i):
                answer.pop()
        else:
            for x in range(i * 2):
                answer.append(i)
    return answer
