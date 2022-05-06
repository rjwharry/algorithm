import sys

# arrangement = [
#     [[0, -1], [1, -1]],
#     [[0, -1], [-1, -1]],
#     [[-1, 0], [-1, -1]],
#     [[-1, 0], [-1, 1]],
#     [[0, 1], [-1, 1]],
#     [[0, 1], [1, 1]],
#     [[1, 0], [1, 1]],
#     [[1, 0], [1, -1]],
#     [[-1, 0], [0, -1]],
#     [[-1, 0], [0, 1]],
#     [[0, 1], [1, 0]],
#     [[0, -1], [1, 0]],
# ]

arrangement = [
    [[0, 1], [1, 1]],
    [[1, 0], [1, 1]],
    [[1, 0], [1, -1]],
    [[0, 1], [1, 0]],
]


def find_start(board):
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == ".":
                return y, x
    return -1, -1


def in_range(H, W, y, x):
    return y >= 0 and y < H and x >= 0 and x < W


def can_go(H, W, board, y, x, y1, x1, y2, x2):
    if not (in_range(H, W, y, x) and in_range(H, W, y1, x1) and in_range(H, W, y2, x2)):
        return False
    return board[y][x] == "." and board[y1][x1] == "." and board[y2][x2] == "."


def print_board(board):
    for row in board:
        for col in row:
            sys.stdout.write(col)
        sys.stdout.write("\n")
    sys.stdout.flush()


def solution(H, W, board):
    y, x = find_start(board)
    if y == -1 and x == -1:
        return 1
    ret = 0
    for method in arrangement:
        move_1, move_2 = method[0], method[1]
        y1, x1 = y + move_1[0], x + move_1[1]
        y2, x2 = y + move_2[0], x + move_2[1]
        if can_go(H, W, board, y, x, y1, x1, y2, x2):
            board[y][x] = board[y1][x1] = board[y2][x2] = "#"
            # print("----------------------")
            # print_board(board)
            # print("----------------------")
            ret += solution(H, W, board)
            board[y][x] = board[y1][x1] = board[y2][x2] = "."
    return ret


if __name__ == "__main__":
    test_case = int(input("Test Case: "))
    H = 0
    W = 0
    for t in range(test_case):
        board = []
        input_list = list(map(int, sys.stdin.readline().split()))
        H, W = input_list[0], input_list[1]
        for i in range(H):
            row = list(sys.stdin.readline().strip())
            board.append(row)
        answer = solution(H, W, board)
        print(answer)
