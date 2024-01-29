def bfs(land, visited, start_i, start_j):
    count = 1
    start = start_j
    end = start_j

    visited[start_i][start_j] = True
    child_list = [(start_i, start_j)]
    while len(child_list) > 0:
        curr_i, curr_j = child_list[0]
        del child_list[0]
        if start > curr_j:
            start = curr_j
        if end < curr_j:
            end = curr_j
        # up
        if (
            curr_i - 1 >= 0
            and not visited[curr_i - 1][curr_j]
            and land[curr_i - 1][curr_j] == 1
        ):
            child_list.append((curr_i - 1, curr_j))
            visited[curr_i - 1][curr_j] = True
            count += 1
        # right
        if (
            curr_j + 1 < len(land[0])
            and not visited[curr_i][curr_j + 1]
            and land[curr_i][curr_j + 1] == 1
        ):
            child_list.append((curr_i, curr_j + 1))
            visited[curr_i][curr_j + 1] = True
            count += 1
        # down
        if (
            curr_i + 1 < len(land)
            and not visited[curr_i + 1][curr_j]
            and land[curr_i + 1][curr_j] == 1
        ):
            child_list.append((curr_i + 1, curr_j))
            visited[curr_i + 1][curr_j] = True
            count += 1
        # left
        if (
            curr_j - 1 >= 0
            and not visited[curr_i][curr_j - 1]
            and land[curr_i][curr_j - 1] == 1
        ):
            child_list.append((curr_i, curr_j - 1))
            visited[curr_i][curr_j - 1] = True
            count += 1
    return start, end, count


def solution(land):
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    oil_group = []

    for col in range(len(land[0])):
        for row in range(len(land)):
            if not visited[row][col] and land[row][col] == 1:
                start, end, count = bfs(land, visited, row, col)
                oil_group.append((start, end, count))

    drilled_list = [0] * len(land[0])
    for group in oil_group:
        for idx in range(group[0], group[1] + 1):
            drilled_list[idx] += group[2]
    return max(drilled_list)


if __name__ == "__main__":
    test_cases = [
        [
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1],
        ],
        [
            [1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
        ],
    ]

    for test_case in test_cases:
        print(solution(test_case))
