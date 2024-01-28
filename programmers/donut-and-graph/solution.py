def get_graph_type(state):
    if state[0] >= 1 and state[1] == 0:
        return 2
    elif state[0] >= 2 and state[1] >= 2:
        return 3
    else:
        return -1


def solution(edges):
    answer = [0, 0, 0, 0]
    # 1. 들어오는게 0개, 나가는게 1개 초과 : 새로운 정점
    # 2. 들어오는게 n개, 나가는게 n개 : 8자 정점
    # 3. 들어오는게 1개, 나가는게 0개 : 막대 정점
    # 4. 그 외 나머지 도넛
    edge_state = {}  # key: [in_cnt, out_cnt]
    for edge_path in edges:
        if edge_path[0] not in edge_state:
            edge_state[edge_path[0]] = [0, 0]
        if edge_path[1] not in edge_state:
            edge_state[edge_path[1]] = [0, 0]

        edge_state[edge_path[0]][1] += 1
        edge_state[edge_path[1]][0] += 1

    graph_cnt = 0
    # print(edge_state)
    for edge, edge_cnt in edge_state.items():
        if edge_cnt[0] == 0 and edge_cnt[1] > 1:
            answer[0] = edge
            graph_cnt = edge_cnt[1]
        graph_type = get_graph_type(edge_cnt)
        if graph_type != -1:
            answer[graph_type] += 1
            # print(edge_cnt, graph_type)

    answer[1] = graph_cnt - answer[2] - answer[3]
    return answer


if __name__ == "__main__":
    test_cases = [
        [[2, 3], [4, 3], [1, 1], [2, 1]],
        [
            [4, 11],
            [1, 12],
            [8, 3],
            [12, 7],
            [4, 2],
            [7, 11],
            [4, 8],
            [9, 6],
            [10, 11],
            [6, 10],
            [3, 5],
            [11, 1],
            [5, 3],
            [11, 9],
            [3, 8],
        ],
    ]
    for test_case in test_cases:
        print(solution(test_case))
