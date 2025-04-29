#코딩 기초 트레이닝
# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
def print_str(str1, str2):
    if 1<=len(str1)<=10 and 1<=len(str2)<=10:
        print(str1 + str2)
        return
    else:
        print("0")
        return
print_str(str1, str2)