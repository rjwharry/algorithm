# 미사일 요격하기
## 풀이  
미사일 시작점, 시작점이 같다면 끝점을 기준으로 오름차순으로 정렬한 후, 한번에 요격할 수 있는 뭉치를 계산  
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181188)
## 더 좋은 풀이
미사일의 끝점을 기준으로 오름차순을 정렬하여 한번에 요격할 수 있는 뭉치를 계산하면,  
로직이 훨씬 간편하고 메모리와 시간복잡도도 더 좋음
```python
def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    answer = 0
    end = -1  # 마지막으로 요격한 미사일의 x좌표

    for s, e in targets:
        if s >= end:  # 이전에 요격한 미사일로는 현재 미사일을 요격할 수 없는 경우
            answer += 1
            end = e  # 현재 미사일을 요격함으로써 끝나는 지점을 업데이트

    return answer
```
