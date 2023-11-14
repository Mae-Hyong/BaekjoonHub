import re

def solution(my_string):
    return sum(sorted(map(int, (list(re.sub('[^0-9]','', my_string))))))