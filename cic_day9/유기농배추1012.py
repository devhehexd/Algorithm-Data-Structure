T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(T):
  M, N, K = map(int, input().split())
  
  cabbages = set()
  for _ in range(K):
    c, r = map(int, input().split())
    cabbages.add((r, c))
  
  count = 0
  
  while cabbages:
    sr, sc = cabbages.pop()
    stack = [(sr, sc)]
    
    while stack:
      r, c = stack.pop()
      
      for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if (nr, nc) in cabbages:
          stack.append((nr, nc))
          cabbages.discard((nr, nc))
    
    count += 1
  
  print(count)