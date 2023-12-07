def solution(num_list):
    mul = 1
    for i in range(len(num_list)):
        mul *= num_list[i]
    if sum(num_list) ** 2 > mul:
        return 1
    return 0