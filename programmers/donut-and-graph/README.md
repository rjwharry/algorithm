# 도넛과 그래프
[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/258711)
## 풀이
- 각 그래프 타입에서 특징을 가진 정점의 개수를 구한다.  
    - 막대: 막대 그래프의 마지막 정점은 항상 나가는게 없다  
    - 8자: 가운데 정점은 항상 n개가 들어오고 n개가 나간다. (n >= 2)
    - 도넛: 모든 정점이 1개가 들어오고 1개가 나간다.
- 이 때 도넛 정점은 막대와 8자 그래프에 참여하는 정점들의 특성과 같으므로 전체 그래프 개수에서  
막대와 8자 그래프 개수를 빼서 구한다.  
- 새로운 정점은 들어오는 거 없이 나가는게 2개 이상이다.

## 오답노트
- 시작을 직관적으로 하는건 좋지만, 여기서 벗어나지 못하고 계속 직접 그래프에 참여하는 정점들을 수집하려 했음