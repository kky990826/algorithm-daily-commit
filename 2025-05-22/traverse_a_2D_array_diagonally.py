#코딩 기초 트레이닝
# 특별한 이차원 배열
def solution(board, k):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k :
                sum += board[i][j]
    return sum