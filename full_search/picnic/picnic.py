from collections import defaultdict
from typing import List, Dict
import sys

used = []


def validate(will_mate: list, mate_map: Dict):
    if will_mate in used:  # 중복 여부 체크
        return False
    for pair in will_mate:  # 짝꿍 가능 여부 체크
        if pair[0] not in mate_map.keys() or pair[1] not in mate_map[pair[0]]:
            return False
    return True


def count_mate(
    student: List[int], will_mate: List[List], mated: List[bool], mate_map: Dict
):
    if all(mated):
        sorted_mate = sorted(will_mate, key=lambda x: x[0])
        if validate(sorted_mate, mate_map):
            used.append(sorted_mate.copy())
            return 1
        else:
            return 0
    pair = []
    ret = 0
    for idx, f_id in enumerate(student):
        if mated[f_id]:
            continue
        pair.append(f_id)
        mated[f_id] = True
        second_student_list = student[idx + 1 :]
        for s_id in second_student_list:
            if not mated[s_id]:
                pair.append(s_id)
                mated[s_id] = True
                will_mate.append(pair.copy())
                ret += count_mate(student, will_mate, mated, mate_map)
                will_mate.pop()
                mated[s_id] = False
                pair.pop()
        mated[f_id] = False
        pair.pop()
    return ret


def solution(student_num: int, mate_list: list):
    mated = [False] * student_num
    student_list = [stu for stu in range(student_num)]
    mate_map = defaultdict(list)
    mate = []
    for idx, student_id in enumerate(mate_list):
        mate.append(student_id)
        if idx % 2 == 1:
            mate.sort()
            mate_map[mate[0]].append(mate[1])
            mate = []
    return count_mate(student_list, [], mated, mate_map)


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
