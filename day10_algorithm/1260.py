import sys
sys.stdin = open("D:\Algorithm_Data_Structure\day10_python_algorithm\input1260.txt")
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V

# input 함수 대체
import sys
input = sys.stdin.readline

N, M, V = list(map(int, input().strip().split()))

# 인접 리스트 표현
graph = []

# N + 1 만큼 빈 리스트 추가
for _ in range(N + 1):
  temp = []
  graph.append(temp)

# M개의 줄 간선의 정보
for _ in range(M):
  # 양방향 간선
  start, end = list(map(int, input().strip().split()))
  graph[start].append(end)
  graph[end].append(start)

for index in range(len(graph)):
  graph[index] = sorted(graph[index])
  
for row in graph:
  print(row)
  

# DFS 구현

# stack = []
# visited = set()

# start = V
# stack.append(start)
# visited.add(start)

# while stack:
#   node = stack.pop()
  
#   # end 인자의 역할
#   # 출력문 마지막 문자를 지정(기본값: 개행문자)
#   print(node, end=" ")
  
#   for adj_node in graph[node]:
#     if adj_node not in visited:
#       visited.add(adj_node)
#       stack.append(adj_node)


def dfs(node):
  print(node, end=" ")
  for adj_node in graph[node]:
    if visited[adj_node] == False:
      visited[adj_node] = True
      dfs(adj_node)

visited = [False] * (N + 1)

start = V
visited[start] = True

dfs(start)

print()


# BFS 구현

from collections import deque

queue = deque()

visited = set()

start = V
queue.append(start)
visited.add(start)

while queue:
  node = queue.popleft()
  
  # end 인자의 역할
  # 출력문 마지막 문자를 지정(기본값: 개행문자)
  print(node, end=" ")
  
  for adj_node in graph[node]:
    if adj_node not in visited:
      visited.add(adj_node)
      queue.append(adj_node)





