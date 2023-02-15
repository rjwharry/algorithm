alphabet_set = "abcdefghijklmnopqrstuvwxyz"

def change_alphabet(origin, skip_idx, index):
    origin_idx = alphabet_set.find(origin)
    to = origin_idx
    while index > 0:
        to += 1
        to %= 26
        if to in skip_idx:
            index += 1
        index -= 1
    return alphabet_set[to]
    
    

def solution(s, skip, index):
    skip_idx = []
    for i in range(len(skip)):
        skip_idx.append(alphabet_set.find(skip[i]))
    skip_idx.sort()
    answer = ''
    for i in range(len(s)):
        new_s = change_alphabet(s[i], skip_idx, index)
        answer += new_s
    return answer