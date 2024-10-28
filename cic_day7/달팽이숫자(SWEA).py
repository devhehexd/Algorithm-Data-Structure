T = int(input())

# 델타 탐색 세팅(dr, dc, 우하좌상 순서)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
  N = int(input())
  # N*N 빈 이차원리스트 제작
  snail = [[0] * N for _ in range(N)]
  
  # 초기 세팅
  r, c, d = 0, 0, 0
  
  # 반목문(1 ~ N*N)
  for num in range(1, N**2 + 1):
    # 숫자 채우고
    snail[r][c] = num
    # 새 좌표 찍기
    nr, nc = r + dr[d], c + dc[d]
    # 유효성 검사(범위, 방문여부)
    if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
      # 유효? => 좌표 갱신(이동)
      r, c = nr,  nc
    # 유효 x? => 방향을 바꾸고 새 좌표로 갱신
    else:
      d = (d + 1) % 4
      r, c = r + dr[d], c + dc[d]
  
  print(f'#{tc}')
  for now in snail:
    print(*now)