import sys
sys.stdin = open("D:\Algorithm_Data_Structure\day10_python_algorithm\input2606.txt")

import sys
input = sys.stdin.readline

# 정점의 수 V
V = int(input())

# 간선의 수 E
E = int(input())

# 인접 리스트 표현
graph = []

for _ in range(V + 1):
  graph.append([])

# 간선의 정보 E 개
for _ in range(E):
  start, end = list(map(int, input().split()))
  graph[start].append(end)
  graph[end].append(start)

# for row in graph:
#   print(row)

start = 1
count = 0

from collections import deque

queue = deque()
visited = set()

queue.append(start)
visited.add(start)

while queue:
  node = queue.popleft()
  
  for adj_node in graph[node]:
    if adj_node not in visited:
      visited.add(adj_node)
      count += 1
      queue.append(adj_node)
      

print(count)