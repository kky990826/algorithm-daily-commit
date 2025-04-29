def solution(my_string, overwrite_string, s):
    my_string = list(my_string)
    overwrite_string = list(overwrite_string)
    my_string[s:s + len(overwrite_string)] = overwrite_string
    #s번째부터 overwrite_string 길이만큼을 리스트 overwrite_string으로 덮어쓰기
    #슬라이싱 => 파이썬의 특수 기능, 리스트여서 가능
    return "".join(my_string)
