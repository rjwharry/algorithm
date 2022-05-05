from collections import defaultdict
import sys


def count_mate(mated, mate_map):
    first_id = -1
    for id, mate in enumerate(mated):
        if not mate:
            first_id = id
            break
    if first_id == -1:
        return 1
    ret = 0
    for id in range(first_id + 1, len(mated)):
        if not mated[id] and id in mate_map[first_id]:
            mated[id] = mated[first_id] = True
            ret += count_mate(mated, mate_map)
            mated[id] = mated[first_id] = False
    return ret


def solution(student_num: int, mate_list: list):
    mated = [False] * student_num
    mate_map = defaultdict(list)
    mate = []
    for idx, student_id in enumerate(mate_list):
        mate.append(student_id)
        if idx % 2 == 1:
            mate.sort()
            mate_map[mate[0]].append(mate[1])
            mate = []
    return count_mate(mated, mate_map)


if __name__ == "__main__":
    test_case = int(input("Test Case: "))
    student_num = 0
    mate_num = 0
    for t in range(test_case):
        input_list = list(map(int, sys.stdin.readline().split()))
        student_num, mate_num = input_list[0], input_list[1]
        mate_list = list(map(int, sys.stdin.readline().split()))
        answer = solution(student_num, mate_list)
        print(answer)
