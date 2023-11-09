def solution(n, k):
    i = n // 10
    k -= i
    return (n * 12000) + (k * 2000)