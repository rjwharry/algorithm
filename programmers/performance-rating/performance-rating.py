def solution(scores):
    answer = 1
    wonho = scores[0]
    wonho_score = sum(wonho)
    scores.sort(key=lambda s : (-s[0], s[1]))
    criteria = -1
    for score in scores:
        if wonho[0] < score[0] and wonho[1] < score[1]:
            return -1
        if criteria <= score[1]:
            if wonho_score < sum(score):
                answer += 1
            criteria = score[1]
    return answer