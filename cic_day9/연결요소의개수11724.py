def DFS(cur):
  # 방문
  # 탐색
  for next in adj_list[cur]:
    if next not in visited:
      visited.add(next)
      DFS(next)
            
N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
  s, e = map(int, input().split())
  adj_list[s].append(e)
  adj_list[e].append(s)

visited = set()
count = 0

# 모든 정점에서 검토
for node in range(1, N + 1):
  # 방문한 적이 없는 정점이라면?
  if node not in visited:
    visited.add(node)
    DFS(node)
    count += 1

print(count)