def solution(rsp):
    result = {'2':'0', '0':'5', '5':'2'}
    return ''.join(result[i] for i in rsp)