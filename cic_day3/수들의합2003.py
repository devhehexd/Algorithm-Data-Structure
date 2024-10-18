import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

s = e = 0
tmp = ans = 0

while True:
  if tmp < M:
    if e == N:
      break
    tmp += nums[e]
    e += 1
  elif tmp > M:
    tmp -= nums[s]
    s += 1
  else:
    ans += 1
    tmp -= nums[s]
    s += 1

print(ans)
    




  