#코딩 기초 트레이닝
# 마지막 두 원소
def solution(num_list):
        if num_list[-1] > num_list[-2]:
            num_list.append(num_list[-1] - num_list[-2])
        else:
            num_list.append(num_list[-1] *2)
        return num_list