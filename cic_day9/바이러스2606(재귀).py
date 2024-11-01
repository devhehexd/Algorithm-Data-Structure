# 재귀
V = int(input())
E = int(input())

# 인접리스트
adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
  s, e = map(int, input().split())
  adj_list[s].append(e)
  adj_list[e].append(s)

# 초기 세팅(출발지, 기록지)
visited = [0] * (V + 1)
visited[1] = 1

# 반복(방문과 탐색)
def DFS(cur):
  visited[cur] = 1
  
  for next in adj_list[cur]:
    if not visited[next]:
      DFS(next)