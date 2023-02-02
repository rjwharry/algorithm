from collections import deque


def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    total = q1_sum + q2_sum
    q1_length = len(queue1)
    q2_length = len(queue2)
    if total % 2 != 0:
        return -1
    answer = 0
    while q1_sum != q2_sum:
        if q1_sum < q2_sum:
            val = deque2.popleft()
            deque1.append(val)
            q1_sum += val
            q2_sum -= val
        else:
            val = deque1.popleft()
            deque2.append(val)
            q1_sum -= val
            q2_sum += val
        if answer > 2 * (q1_length + q2_length):
            return -1
        answer += 1
    return answer
