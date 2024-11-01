import sys
from collections import deque

sys.stdin = open("D:\Algorithm_Data_Structure\cic_day9\input(미로SWEA).txt")

import sys

input = sys.stdin.readline

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
  N = int(input())
  maze = [list(map(int, input().strip())) for _ in range(N)]
  
  # 초기 세팅(출발지, 기록지, 예정지)
  flag = False
  for r in range(N):
    for c in range(N):
      if maze[r][c] == 2:
        sr, sc = r, c
        flag = True
        break
    if flag:
      break
    
  visited = set([(sr, sc)])
  queue = deque([(sr, sc, -1)])
  ans = 0

  # 방문-탐색의 반복
  while queue:
    # 방문
    r, c, count = queue.popleft()
    if maze[r][c] == 3:
      ans = count
      break
    
    # 탐색
    for d in range(4):
      nr, nc = r + dr[d], c + dc[d]
      
      if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited and maze[nr][nc] != 1:
        visited.add((nr, nc))
        queue.append((nr, nc, count + 1))
  
  print(f'#{tc} {ans}')