from collections import defaultdict
import sys

def is_all_mated(mated_list):
    ret = True
    for mated in mated_list:
        if not mated:
            ret = False
    return ret

def count_mate(student_list, mated_list, mate_map):
    if is_all_mated(mated_list):
        return 1
    
def solution(student_num, mate_list):
    mated_list = [False] * student_num
    student_list = [stu for stu in range(student_num)]
    mate_map = defaultdict(list)
    mate = []
    for idx, student_id in enumerate(mate_list):
        mate.append(student_id)
        if idx % 2 == 1:
            mate.sort()
            mate_map[mate[0]].append(mate[1])
            mate = []


if __name__ == "__main__":
    test_case = int(input("Test Case: "))
    student_num = 0
    mate_num = 0
    for t in range(test_case):
        input_list = list(map(int, sys.stdin.readline().split()))
        student_num, mate_num = input_list[0], input_list[1]
        for m in range(mate_num):
            mate_list = list(map(int, sys.stdin.readline().split()))
            answer = solution(student_num, mate_list)
            print(answer)