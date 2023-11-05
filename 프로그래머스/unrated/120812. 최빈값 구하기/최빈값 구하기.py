from collections import Counter
def solution(array):
    counter = Counter(array)
    max_count = max(counter.values())
    mode = [key for key, value in counter.items() if value == max_count]

    if len(mode) > 1:
        return -1
    else:
        return mode[0]