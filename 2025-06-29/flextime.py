def to_minutes(t):
    return (t // 100) * 60 + (t % 100)

def solution(schedules, timelogs, startday):
    WEEKEND = {0, 6}
    answer = 0
    n = len(schedules)

    for i in range(n):
        hope = schedules[i]
        success = True
        for d in range(7):
            day_index = (startday + d) % 7
            if day_index in WEEKEND:
                continue
            attend = timelogs[i][d]
            if to_minutes(attend) > to_minutes(hope) + 10:
                success = False
                break
        if success:
            answer += 1
    return answer

