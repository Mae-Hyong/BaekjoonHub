def solution(numbers, direction):
    answer = 0
    if direction == "left":
        answer = numbers[1:] + [numbers[0]]
    else:
        answer = [numbers[-1]] + numbers[:len(numbers)-1]
    return answer