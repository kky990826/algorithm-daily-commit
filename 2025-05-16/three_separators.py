#코딩 기초 트레이닝
# 세 개의 구분자
import re

def solution(myStr):
    result = re.split(r'[abc]', myStr)
    results = [s for s in result if s != '']
    if results:
        return results
    else:
        return ["EMPTY"]
