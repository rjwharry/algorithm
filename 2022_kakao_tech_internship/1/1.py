score_chart = [-1, 3, 2, 1, 0, 1, 2, 3]


def get_result(type_1, type_2, score_map):
    return type_1 if score_map.get(type_1, 0) >= score_map.get(type_2, 0) else type_2


def solution(survey, choices):
    answer = ""
    score_map = {}
    for idx, choice in enumerate(choices):
        candidate = survey[idx]
        category = ""
        if choice > 4:
            category = candidate[1]
        elif choice < 4:
            category = candidate[0]
        else:
            continue
        score = score_map.get(category, 0)
        score += score_chart[choice]
        score_map[category] = score
    answer += get_result("R", "T", score_map)
    answer += get_result("C", "F", score_map)
    answer += get_result("J", "M", score_map)
    answer += get_result("A", "N", score_map)
    return answer
