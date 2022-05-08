from distutils.ccompiler import new_compiler
import sys

MAX_CNT = 100

button = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13],
]


def is_clock_sync(clock):
    for t in clock:
        if t != 12 and t != 0:
            return False
    return True


def push_button(clock, switch_num):
    new_clock = clock.copy()
    targets = button[switch_num]
    for target in targets:
        new_clock[target] = (clock[target] + 3) % 12
    return new_clock


def min_button_count(clock, switch_num):
    if switch_num == 10:
        if is_clock_sync(clock):
            return 0
        else:
            return MAX_CNT
    ret = MAX_CNT
    pushed_clock = clock.copy()
    for push_cnt in range(4):
        ret = min(ret, push_cnt + min_button_count(pushed_clock, switch_num + 1))
        pushed_clock = push_button(pushed_clock, switch_num)
    return ret


if __name__ == "__main__":
    test_case = int(input("Test Case: "))
    visited = [False] * 16
    for t in range(test_case):
        clock = list(map(int, sys.stdin.readline().split()))
        answer = min_button_count(clock, 0)
        print(answer)
