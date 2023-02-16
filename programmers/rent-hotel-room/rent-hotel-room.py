def add_ten_minute(book_time):
    hour_str = minute_str = ""
    hour, minute = book_time.split(":")
    hour = int(hour)
    minute = int(minute) + 10
    if minute >= 60:
        minute -= 60
        hour += 1
    if int(minute / 10) == 0:
        minute_str = "0"
    if int(hour / 10) == 0:
        hour_str = "0"
    return hour_str + str(hour) + ":" + minute_str + str(minute)

def find_next(last_time, sorted_book_time, visited):
    can_start_time = add_ten_minute(last_time)
    # print(last_time, can_start_time)
    for idx, book_time in enumerate(sorted_book_time):
        if not visited[idx] and book_time[0] >= can_start_time:
            return idx
    return -1
            

def solution(book_time):
    answer = 0
    sorted_book_time = sorted(book_time, key=lambda book: book[0])
    visited = [False] * len(book_time)
    idx = 0
    
    while not all(visited):
        visited[idx] = True
        last_time = sorted_book_time[idx][1]
        idx = find_next(last_time, sorted_book_time, visited)
        if idx == -1:
            answer += 1
            if all(visited):
                break
            idx = visited.index(False)
        
    return answer