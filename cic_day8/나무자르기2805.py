import sys
input = sys.stdin.readline


def binary_search(l, r):
  c = (l + r) // 2
  
  while l <= r:
    # c를 기준으로 나무 길이 계산
    cnt = sum([tree - c for tree in trees if tree > c])

    if cnt >= M:
      l = c + 1
      
    elif cnt < M:
      r = c - 1
      
    else:
      return(c)
    
    c = (1 + r) // 2
  
  return(c)
N, M = map(int, input().split())

trees = list(map(int, input().split()))

binary_search(0, max(trees))

