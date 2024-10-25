T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
  N, M = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(M)]

  # 최대값 초기값
  ans = float("INF")
  
  # 이차원 리스트 순회
  for r in range(N):
    for c in range(M):
      # 델타 탐색(임시 값 계산, 범위 검토)
      tmp = matrix[r][c]
      for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
          tmp += matrix[nr][nc]
    
      # 최대값 갱신
      ans = max(ans, tmp)
      
  print(f'#{tc} {ans}')