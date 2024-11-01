T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
  N = int(input())
  maze = [[1] * (N + 2) for _ in range(N + 2)]
  for i in range(1, N + 1):
    maze[i][1 : N + 1] = list(map(int, input().split()))
    
  
  # 초기 세팅(출발지, 기록지, 예정지)
  flag = False
  for r in range(1, N + 1):
    for c in range(1, N + 1):
      if maze[r][c] == 2:
        sr, sc = r, c
        flag = True
        break
    if flag:
      break
    
  visited = set([(sr, sc)])
  stack = [(sr, sc)]
  ans = 0

  # 방문-탐색의 반복
  while stack:
    # 방문
    r, c = stack.pop()
    if ans:
      break
    
    # 탐색
    for d in range(4):
      nr, nc = r + dr[d], c + dc[d]
      if maze[nr][nc] == 3:
        ans = 1
        break
      
      if maze[nr][nc] != 1:
        stack.append((nr, nc))
        maze[nr][nc] = 1
  
  print(f'{tc} {ans}')