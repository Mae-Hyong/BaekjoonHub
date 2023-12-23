def solution(myString, pat):
    return sum(1 for _ in range(len(myString) - len(pat) + 1) if myString.startswith(pat, _))