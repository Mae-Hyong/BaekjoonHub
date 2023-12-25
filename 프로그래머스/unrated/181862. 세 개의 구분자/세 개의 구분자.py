def solution(myStr):
    parts = myStr.replace('b', 'a').replace('c', 'a').split('a')
    filtered = list(filter(None, map(str, parts)))
    return filtered if filtered else ["EMPTY"]