from collections import defaultdict
import sys

MAX_WEIGHT = 20 * 1000 * 1000


def print_courses(courses):
    for row in courses:
        for val in row:
            if val == MAX_WEIGHT:
                val = "X"
            else:
                val = str(val)
            sys.stdout.write(val)
            sys.stdout.write("\t")
        sys.stdout.write("\n")
    sys.stdout.flush()


def dfs_backup(courses, cur, dist, gates, summits, visited, weight_list, cache):
    if cur == dist:
        max_weight = max(weight_list)
        # print(weight_list)
        return max_weight
    visited[cur] = True
    # ret = MAX_WEIGHT
    ret = cache[cur][dist]
    if ret != MAX_WEIGHT:
        return max(ret, max(weight_list))
    adj_list = [p for p in range(len(courses)) if courses[cur][p] != MAX_WEIGHT]
    for next_point in adj_list:
        curr_weight = courses[cur][next_point]
        if not visited[next_point] and curr_weight != MAX_WEIGHT:
            # print(str(cur) + " -> " + str(next_point) + " : " + str(courses[cur][next_point]))
            print(str(cur) + " -> " + str(next_point))
            if next_point in summits or next_point in gates:
                continue
            if curr_weight > ret:
                continue
            weight_list.append(curr_weight)
            result = dfs(
                courses, next_point, dist, gates, summits, visited, weight_list, cache
            )
            weight_list.pop(-1)
            ret = min(ret, result)
    visited[cur] = False
    cache[cur][dist] = ret
    return ret


def dfs(courses, cur, dist, gates, summits, visited, cache):
    if cur == dist:
        return 0
    visited[cur] = True
    ret = cache[cur][dist]
    if ret != MAX_WEIGHT:
        return ret
    adj_list = [p for p in range(len(courses)) if courses[cur][p] != MAX_WEIGHT]
    for next_point in adj_list:
        cur_weight = courses[cur][next_point]
        if (
            not visited[next_point]
            and cur_weight != MAX_WEIGHT
            and (len(summits) == 0 or next_point not in summits)
            and (len(gates) == 0 or next_point not in gates)
        ):
            result = dfs(courses, next_point, dist, gates, summits, visited, cache)
            partial_max = max(cur_weight, result)
            ret = min(ret, partial_max)
    cache[cur][dist] = ret
    visited[cur] = False
    return ret


def solution(n, paths, gates, summits):
    answer = []
    row = [MAX_WEIGHT] * (n + 1)
    courses = []
    cache = []
    for i in range(n + 1):
        courses.append(row.copy())
        cache.append(row.copy())
    for path in paths:
        y = path[0]
        x = path[1]
        weight = path[2]
        courses[y][x] = weight
        courses[x][y] = weight
    intensity_map = {}
    for summit in summits:
        intensity = intensity_map.get(summit, MAX_WEIGHT)
        for gate in gates:
            visited = [False] * (n + 1)
            summits_temp = summits.copy()
            summits_temp.remove(summit)
            # print("start:", gate, "summit:", summit)
            result = dfs(courses, gate, summit, gates, summits_temp, visited, cache)
            # print(gate, summit, result)
            intensity = min(intensity, result)
        intensity_map[summit] = intensity
    print_courses(cache)

    min_intensity = MAX_WEIGHT
    min_summit = -1
    summits.sort()
    for summit in summits:
        curr_intensity = intensity_map[summit]
        if min_intensity > curr_intensity:
            min_intensity = curr_intensity
            min_summit = summit
    answer.append(min_summit)
    answer.append(min_intensity)
    return answer


if __name__ == "__main__":
    # n = 7
    # paths = (
    #     [1, 2, 5],
    #     [1, 4, 1],
    #     [2, 3, 1],
    #     [2, 6, 7],
    #     [4, 5, 1],
    #     [5, 6, 1],
    #     [6, 7, 1],
    # )
    # gates = [3, 7]
    # summits = [1, 5]
    n = 8
    paths = (
        [1, 2, 1],
        [1, 3, 2],
        [1, 4, 5],
        [1, 5, 1],
        [2, 6, 3],
        [3, 6, 4],
        [4, 7, 2],
        [5, 7, 2],
        [6, 8, 2],
        [7, 8, 1],
    )
    gates = [1]
    summits = [8]
    print(solution(n, paths, gates, summits))
