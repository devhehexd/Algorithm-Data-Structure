# 재귀 스택 오버플로우 방지

import sys
sys.setrecursionlimit(10**9)

def recursion_func(depth):
  if depth == 1500:
    return
  print(f"kekw {depth}")
  recursion_func(depth + 1)

recursion_func(1)

# 시스템 스택
def find(depth):
  if depth == 10:
    print("찾았다")
    return
  print(f"내려가는 중.. 깊이: {depth}")
  
  find(depth + 1)
  
  print(depth)

find(0)