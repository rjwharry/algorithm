SIZE = 51
UPDATE = "UPDATE"
MERGE = "MERGE"
UNMERGE = "UNMERGE"
PRINT = "PRINT"
EMPTY = "EMPTY"


def update(chart, group, p, val):
    for idx, g in enumerate(group):
        if g == group[p]:
            chart[idx] = val


def replace_all(chart, val1, val2):
    for idx, val in enumerate(chart):
        if val == val1:
            chart[idx] = val2


def merge(chart, group, p1, p2):
    if p1 == p2:
        return
    value = chart[p2] if chart[p1] == EMPTY and chart[p2] != EMPTY else chart[p1]
    for idx, g in enumerate(group):
        if g == group[p2]:
            group[idx] = group[p1]
    for idx, g in enumerate(group):
        if g == group[p1]:
            chart[idx] = value


def unmerge(chart, group, p):
    value = chart[p]
    for idx, g in enumerate(group):
        if g == group[p]:
            group[idx] = idx
            chart[idx] = EMPTY
    chart[p] = value


def calculate_idx(r, c):
    return SIZE * int(r) + int(c)


def solution(commands):
    chart = [EMPTY for _ in range((SIZE) ** 2)]
    group = [i for i in range((SIZE) ** 2)]
    answer = []
    for command in commands:
        token = command.split(" ")
        cmd = token[0]
        if cmd == UPDATE:
            if len(token) == 4:
                update(chart, group, calculate_idx(token[1], token[2]), token[3])
            else:
                replace_all(chart, token[1], token[2])
        elif cmd == MERGE:
            merge(
                chart,
                group,
                calculate_idx(token[1], token[2]),
                calculate_idx(token[3], token[4]),
            )
        elif cmd == UNMERGE:
            unmerge(chart, group, calculate_idx(token[1], token[2]))
        elif cmd == PRINT:
            answer.append(chart[calculate_idx(token[1], token[2])])
    return answer


if __name__ == "__main__":
    input_list = [
        [
            "UPDATE 1 1 menu",
            "UPDATE 1 2 category",
            "UPDATE 2 1 bibimbap",
            "UPDATE 2 2 korean",
            "UPDATE 2 3 rice",
            "UPDATE 3 1 ramyeon",
            "UPDATE 3 2 korean",
            "UPDATE 3 3 noodle",
            "UPDATE 3 4 instant",
            "UPDATE 4 1 pasta",
            "UPDATE 4 2 italian",
            "UPDATE 4 3 noodle",
            "MERGE 1 2 1 3",
            "MERGE 1 3 1 4",
            "UPDATE korean hansik",
            "UPDATE 1 3 group",
            "UNMERGE 1 4",
            "PRINT 1 3",
            "PRINT 1 4",
        ],  # ["EMPTY", "group"]
        [
            "MERGE 1 1 1 2",
            "MERGE 1 1 2 1",
            "MERGE 1 1 2 2",
            "UPDATE 3 3 b",
            "UPDATE 2 3 a",
            "PRINT 1 1",
            "MERGE 1 1 3 3",
            "PRINT 1 1",
            "PRINT 1 2",
            "MERGE 1 1 2 3",
            "PRINT 2 3",
            "UNMERGE 2 3",
            "PRINT 2 3",
            "PRINT 1 1",
        ],  # ["EMPTY", "b", "b", "b", "b", "EMPTY"]
        [
            "UPDATE 1 1 a",
            "UPDATE 1 2 a",
            "UPDATE 2 1 a",
            "UPDATE 2 2 a",
            "UPDATE 3 3 b",
            "UPDATE 3 4 b",
            "UPDATE 4 3 b",
            "UPDATE 4 4 b",
            "PRINT 4 4",
            "MERGE 1 1 1 2",
            "MERGE 1 1 2 2",
            "MERGE 1 1 2 1",
            "MERGE 3 3 3 4",
            "MERGE 3 3 4 3",
            "MERGE 3 3 4 4",
            "UNMERGE 3 4",
            "PRINT 1 1",
            "PRINT 3 4",
        ],  # ['b', 'a', 'b']
        [
            "UPDATE 1 1 A",
            "UPDATE 2 2 B",
            "UPDATE 3 3 C",
            "UPDATE 4 4 D",
            "MERGE 1 1 2 2",
            "MERGE 3 3 4 4",
            "MERGE 1 1 4 4",
            "UNMERGE 3 3",
            "PRINT 1 1",
            "PRINT 2 2",
            "PRINT 3 3",
            "PRINT 4 4",
        ],  # ["EMPTY", 'EMPTY', 'A', 'EMPTY']
        [
            "UPDATE 3 3 a",
            "MERGE 1 1 1 2",
            "MERGE 1 1 2 1",
            "MERGE 1 2 2 2",
            "MERGE 2 2 3 3",
            "MERGE 3 3 3 3",
            "MERGE 3 3 3 4",
            "PRINT 1 1",
            "UNMERGE 1 1",
            "PRINT 1 1",
            "PRINT 2 2",
            "PRINT 3 4",
        ],  # a, a, EMPTY, EMPTY
        [
            "UPDATE 1 1 a",
            "UPDATE 1 2 b",
            "UPDATE 1 3 c",
            "UPDATE 1 4 d",
            "UPDATE 1 5 e",
            "MERGE 1 1 2 2",
            "MERGE 2 2 3 3",
            "MERGE 2 2 4 4",
            "MERGE 4 4 5 5",
            "MERGE 1 2 2 3",
            "MERGE 2 3 3 4",
            "MERGE 2 3 4 5",
            "MERGE 1 3 2 4",
            "MERGE 1 3 3 5",
            "MERGE 1 4 2 5",
            "MERGE 1 5 1 5",
            "PRINT 1 5",
            "PRINT 2 2",
            "UPDATE a z",
            "PRINT 2 2",
            "MERGE 1 1 4 5",
            "PRINT 3 4",
            "UNMERGE 3 4",
            "PRINT 3 4",
            "UNMERGE 3 4",
            "PRINT 3 4",
        ],
    ]
    for input in input_list:
        print(solution(input))
