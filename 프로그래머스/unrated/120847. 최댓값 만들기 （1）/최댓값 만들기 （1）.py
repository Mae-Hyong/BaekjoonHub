def solution(numbers):
    return max(numbers) * sorted(numbers, reverse = True)[1]