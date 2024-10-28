T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
  N, M = map(int, input().split())
  
  # 상하좌우가 0으로 둘러쌓인 2차원 리스트(꼭 0일 필요는 없음)
  matrix = [[0] * (M + 2) for _ in range(N + 2)]
  for i in range(1, N + 1):
    matrix[i][1 : M + 1] = list(map(int, input().split()))
    
  ans = -float("INF")
  
  for r in range(1, N + 1):
    for c in range(1, M + 1):
      tmp = matrix[r][c]
      for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        tmp += matrix[nr][nc]
      
      ans = max(ans, tmp)
      
  print(f'#{tc} {ans}')
    