def find_cluster(targets: list, current_target: list, current_idx: int) -> int:
    next_idx = current_idx + 1
    limit = current_target[1]
    for idx in range(current_idx + 1, len(targets)):
        if targets[idx][0] < limit:
            next_idx = idx + 1
            limit = targets[idx][1] if limit > targets[idx][1] else limit
        else:
            break
    return next_idx


def solution(targets: list):
    answer = 0
    targets.sort(key=lambda target: (target[0], target[1]))
    idx = 0
    while idx < len(targets):
        answer += 1
        idx = find_cluster(targets, targets[idx], idx)

    return answer


if __name__ == "__main__":
    test_cases = [
        [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]],
        [[0, 1], [1, 2], [2, 3], [3, 4], [3, 4]],
        [[0, 1], [0, 1], [0, 1], [1, 3], [2, 3]],
        [[1, 3], [0, 1], [0, 1], [0, 1], [2, 3]],
        [[0, 1], [1, 10], [2, 3], [4, 5], [9, 10]],
        [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]],
        [[0, 2]],
        [[0, 10], [1, 2], [2, 3], [3, 4], [4, 5]],
    ]
    for test_case in test_cases:
        print(solution(test_case))
