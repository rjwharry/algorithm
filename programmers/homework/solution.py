def time_diff(time_a: str, time_b: str):
    hour_a, minute_a = list(map(int, time_a.split(":")))
    hour_b, minute_b = list(map(int, time_b.split(":")))
    return (hour_b * 60 + minute_b) - (hour_a * 60 + minute_a)


def solution(plans: list):
    answer = []
    stack = []
    plans.sort(key=lambda plan: plan[1])
    plans = list(map(lambda plan: [plan[0], plan[1], int(plan[2])], plans))
    for idx in range(len(plans)):
        if idx == len(plans) - 1:
            answer.append(plans[idx][0])
            break
        diff = time_diff(plans[idx][1], plans[idx + 1][1])
        if diff == plans[idx][2]:
            answer.append(plans[idx][0])
        elif diff > plans[idx][2]:
            answer.append(plans[idx][0])
            diff -= plans[idx][2]
            while len(stack) > 0 and diff > 0:
                latest = stack.pop()
                duration = latest[2]
                if diff < latest[2]:
                    latest[2] -= diff
                    stack.append(latest)
                else:
                    answer.append(latest[0])
                diff -= duration
        else:
            plans[idx][2] -= diff
            stack.append(plans[idx])

    while len(stack) > 0:
        answer.append(stack.pop()[0])

    return answer


if __name__ == "__main__":
    test_cases = [
        [  # korean, english, math
            ["korean", "11:40", "30"],
            ["english", "12:10", "20"],
            ["math", "12:30", "40"],
        ],
        [  # science, history, computer, music
            ["science", "12:40", "50"],
            ["music", "12:20", "40"],
            ["history", "14:00", "30"],
            ["computer", "12:30", "100"],
        ],
        [  # b, a, c
            ["a", "00:00", "40"],
            ["b", "00:10", "50"],
            ["c", "23:00", "100"],
        ],
        [  # c, b, a, d
            ["a", "00:01", "100"],
            ["b", "00:02", "100"],
            ["c", "00:03", "100"],
            ["d", "23:59", "100"],
        ],
        [  # a, b, c, d
            ["a", "00:01", "2"],
            ["b", "00:12", "1"],
            ["c", "00:20", "2"],
            ["d", "00:31", "1"],
        ],
        [  # c, d, b, a
            ["a", "00:00", "70"],
            ["b", "00:10", "70"],
            ["c", "00:20", "10"],
            ["d", "01:29", "1"],
        ],
    ]
    for test_case in test_cases:
        print(solution(test_case))
