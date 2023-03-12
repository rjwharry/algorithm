MIN_VALUE = -100001 * 250000


def get_max_sum(sequence):
    max_values = [MIN_VALUE] * len(sequence)
    max_values[0] = sequence[0]
    for idx, val in enumerate(sequence):
        if idx == 0:
            continue
        max_values[idx] = max(max_values[idx - 1] + val, val)
    return max(max_values)


def solution(sequence):
    answer = 0
    positive_pulse = [1, -1]
    negative_pulse = [-1, 1]
    positive_sequence = [ele * positive_pulse[i % 2] for i, ele in enumerate(sequence)]
    negative_sequence = [ele * negative_pulse[i % 2] for i, ele in enumerate(sequence)]
    answer = max(get_max_sum(positive_sequence), get_max_sum(negative_sequence))
    return answer


if __name__ == "__main__":
    inputs = [[2, 3, -6, 1, 3, -1, 2, 4], [2, -2, 2, 2, 10, 1, 1]]
    for input in inputs:
        print(solution(input))
