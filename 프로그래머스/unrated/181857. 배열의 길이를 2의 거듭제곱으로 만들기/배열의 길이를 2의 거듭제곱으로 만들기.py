def solution(arr):
    i = 1
    while len(arr) > i:
        i *= 2 
    for j in range(len(arr), i):
        arr.append(0)
    return arr