def solution(a, b):
    if int(f"{a}{b}") > 2*a*b or int(f"{a}{b}") == 2*a*b:
        return int(f"{a}{b}")
    elif int(f"{a}{b}") < 2*a*b:
        return 2*a*b