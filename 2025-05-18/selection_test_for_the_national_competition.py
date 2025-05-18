#코딩 기초 트레이닝
# 전국 대회 선발 고사
def solution(rank, attendance):
    new_rank = []
    new_rank2 = []
    count = 0
    for i in range(len(rank)):
        if attendance[i] == True:
            new_rank.append(rank[i])
    while (count < 3):
        if min(new_rank) in rank:
            new_rank2.append(rank.index(min(new_rank)))
            new_rank.remove(min(new_rank))
            count +=1
    return new_rank2[0] * 10000 + new_rank2[1] * 100 + new_rank2[2]