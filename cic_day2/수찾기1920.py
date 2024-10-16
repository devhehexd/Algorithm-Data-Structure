N = int(input())
A = set(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

for X in B:
  if X in A:
    print(1)
  else:
    print(0)