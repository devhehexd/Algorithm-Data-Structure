import sys

N, M  = list(map(int, sys.stdin.readline().strip().split()))

# N개의 수열 입력
numbers = list(map(int, sys.stdin.readline().strip().split()))

# 누적합 계산
# 누적합을 저장할 빈 리스트
S = []

# 첫 번째 누적합 저장
# S[0] = numbers[0]
S.append(numbers[0])

# n번째 누적합을 계산
for n in range(1, N):
  # S[n] = S[n - 1] + numbers[n]
  S.append(S[n - 1] + numbers[n])

# M개 줄 만큼 i와 j 입력
for _ in range(M):
  i, j = list(map(int, sys.stdin.readline().strip().split()))
  
  i = j - 1
  j = j - 1
  
  if i != 0:
    numbers = S[j] - S[i - 1]  
    print(numbers)
  elif i == 0:
    numbers = S[j]
