from collections import deque

V = int(input())
E = int(input())

# 1. 빈 판 만들기
adj_matrix = [[0] * V for _ in range(V + 1)]

# 2. 간선 정보 입력 받기
for _ in range(E):
  s, e = map(int, input().split())
  adj_matrix[s][e] = 1
  adj_matrix[e][s] = 1


# 세팅(출발지, 기록지, 예정지)
queue = deque([1])
visited = set([1])

# 그래프 탐색(방문-탐색 반복)
while queue:
  # 방문
  cur = queue.popleft()
  
  # 탐색(인접 행렬)
  for nxt in range(1, V + 1):
    if adj_matrix[cur][nxt] and nxt not in visited:
      visited.add(nxt)
      queue.append(nxt)

