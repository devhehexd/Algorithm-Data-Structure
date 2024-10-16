import sys
input = sys.stdin.readline

N = int(input())

company = set()

for _ in range(N):
  name, log = input().strip().split()
  
  if log == 'enter':
    company.add(name)
  else:
    company.discard(name)

for name in sorted(company, reverse=True):
  print(name)  
