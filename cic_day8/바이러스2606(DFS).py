# 인접 리스트 방식 구조화
V = int(input())
E = int(input())

# 1. 빈 판 만들기
adj_list = [[] for _ in range(V + 1)]

# 2. 간선 정보 입력 받기
for _ in range(E):
  s, e = map(int, input().split())
  adj_list[s].append(e)
  adj_list[e].append(s)


# 세팅(출발지, 기록지, 예정지)
# 여기서는 set 대신 비트마스킹 방식으로 방문한 곳은 1, 안한곳은 0로 표시
stack = [1]
visited = [0] * (V + 1)
visited[1] = 1

# 그래프 탐색(방문-탐색 반복)
while stack: # 스택이 빌 때까지
  # 방문
  cur = stack.pop()
  
  # 탐색(인접 리스트)
  for nxt in adj_list[cur]:
    if visited[nxt] == 0: # if not visited[nxt]
      visited[nxt] = 1
      stack.append(nxt)

