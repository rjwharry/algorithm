import sys
import copy


def shift_row(rc):
    row = len(rc)
    col = len(rc[0])
    row_arr = [0] * col
    new_rc = []
    for r in range(row):
        new_rc.append(row_arr.copy())
    row_length = len(rc)
    for r_idx in range(row_length):
        new_rc[((r_idx + 1) % row_length)] = rc[r_idx]
    return new_rc


def rotate(rc):
    row = len(rc)
    col = len(rc[0])
    prev_val = rc[0][0]
    # move right
    for idx in range(1, col):
        # new_rc[0][idx] = rc[0][idx - 1]
        next_val = rc[0][idx]
        rc[0][idx] = prev_val
        prev_val = next_val
        # print_rc(rc)
        # print("*****************************")
    # move down
    for idx in range(1, row):
        # new_rc[idx][col-1] = rc[idx-1][col-1]
        next_val = rc[idx][col - 1]
        rc[idx][col - 1] = prev_val
        prev_val = next_val
        # print_rc(rc)
        # print("*****************************")
    # move left
    for idx in range(col - 2, -1, -1):
        # new_rc[row-1][idx] = rc[row-1][idx+1]
        next_val = rc[row - 1][idx]
        rc[row - 1][idx] = prev_val
        prev_val = next_val
        # print_rc(rc)
        # print("*****************************")
    # move up
    for idx in range(row - 2, -1, -1):
        # new_rc[idx][0] = rc[idx+1][0]
        next_val = rc[idx][0]
        rc[idx][0] = prev_val
        prev_val = next_val
        # print_rc(rc)
        # print("*****************************")


def print_rc(rc):
    for row in rc:
        for val in row:
            sys.stdout.write(str(val))
            sys.stdout.write(" ")
        sys.stdout.write("\n")
    sys.stdout.flush()


def solution(rc, operations):
    answer = [[]]
    for operation in operations:
        if operation == "Rotate":
            rotate(rc)
        else:
            rc = shift_row(rc)
        # print_rc(rc)
        # print("---------------")
    answer = rc
    return answer
