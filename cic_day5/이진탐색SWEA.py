def binary_search(l, r, target, cnt):
  # 0. 가운데 집기
  c = int((l + r) / 2)
  
  # 1. 정확히 탐색한 경우: cnt 반환
  if target == c:
    return cnt
  
  # 2. 찾은 값이 타겟보다 클 때: 왼쪽 절반
  elif c > target:
    return binary_search(l, c, target, cnt + 1)
    
  # 3. 찾은 값이 타겟보다 작을 때: 오른쪽 절반
  elif c< target:
    return binary_search(c, r, target, cnt + 1)
  
T = int(input())

for tc in range(1, T + 1):
  P, A, B = map(int, input().split())
  cnt_A = binary_search(0, P, A, 0)
  cnt_B = binary_search(0, P, B, 0)
  
  ans = 0 if cnt_A == cnt_B else "A" if cnt_A < cnt_B else 'B'
  print(ans)
  