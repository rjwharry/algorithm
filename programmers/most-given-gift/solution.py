def make_jisoo(gifts, f_index):
    j = [0] * len(f_index)
    for gift in gifts:
        sender, receiver = gift.split()
        j[f_index[sender]] += 1
        j[f_index[receiver]] -= 1
    return j


def make_table(gifts, f_index):
    t = [[0 for _ in range(len(f_index))] for _ in range(len(f_index))]
    for gift in gifts:
        sender, receiver = gift.split()
        t[f_index[sender]][f_index[receiver]] += 1
    return t


def calc_most_received(t, j):
    receive_cnt = [0] * len(j)
    for sender in range(len(j)):
        for receiver in range(len(j)):
            if sender == receiver:
                continue
            if t[sender][receiver] > t[receiver][sender]:
                receive_cnt[sender] += 1
            elif t[sender][receiver] == t[receiver][sender]:
                if j[sender] > j[receiver]:
                    receive_cnt[sender] += 1
    return receive_cnt


def solution(friends, gifts):
    f_index = {friends[i]: i for i in range(len(friends))}
    t = make_table(gifts, f_index)
    j = make_jisoo(gifts, f_index)
    cnt = calc_most_received(t, j)
    return max(cnt)
