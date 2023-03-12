import sys

sys.setrecursionlimit(10000)


def calculate_dist(cr, cc, r, c):
    return abs(r - cr) + abs(c - cc)


def escape(cache, n, m, cr, cc, r, c, k, route, route_list):
    if k < 0:
        return False
    if k == 0 and cr == r and cc == c:
        route_list.append(route)
        return True

    if calculate_dist(cr, cc, r, c) > k:
        return False

    result = cache[cr][cc]
    if len(result) > 0:
        for r in result:
            if r[0] == k:
                return r[1]

    # go down
    if cr + 1 <= n:
        if escape(cache, n, m, cr + 1, cc, r, c, k - 1, route + "d", route_list):
            cache[cr][cc].add((k, True))
            return True
    # go left
    if cc - 1 > 0:
        if escape(cache, n, m, cr, cc - 1, r, c, k - 1, route + "l", route_list):
            cache[cr][cc].add((k, True))
            return True
    # go right
    if cc + 1 <= m:
        if escape(cache, n, m, cr, cc + 1, r, c, k - 1, route + "r", route_list):
            cache[cr][cc].add((k, True))
            return True
    # go up
    if cr - 1 > 0:
        if escape(cache, n, m, cr - 1, cc, r, c, k - 1, route + "u", route_list):
            cache[cr][cc].add((k, True))
            return True
    cache[cr][cc].add((k, False))
    return False


def solution(n, m, x, y, r, c, k):
    answer = ""
    cache = [[set() for _ in range(int(m) + 1)] for _ in range(int(n) + 1)]
    route_list = []
    shortest_length = abs(r - x) + abs(c - y)
    can_go = (shortest_length % 2) == (k % 2)
    if k >= shortest_length and can_go:
        escape(cache, n, m, x, y, r, c, k, "", route_list)
    if len(route_list) == 0:
        answer = "impossible"
    else:
        answer = sorted(route_list)[0]
    return answer


if __name__ == "__main__":
    n = [3, 2, 3]
    m = [4, 2, 3]
    x = [2, 1, 1]
    y = [3, 1, 2]
    r = [3, 2, 3]
    c = [1, 2, 3]
    k = [5, 2, 4]
    for i, _ in enumerate(n):
        print(solution(n[i], m[i], x[i], y[i], r[i], c[i], k[i]))
