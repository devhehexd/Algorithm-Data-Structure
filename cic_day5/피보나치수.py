import sys

# 시간복잡도가 O(2^N)이므로 매우 비효율적
def fibo(N):
    
  # 종료 조건
  if N <= 1:
    return N
    
  # 반복되는 로직
  return fibo(N - 1) + fibo(N - 2)

input = sys.stdin.readline
n = int(input())
print(fibo(n))

# 메모이제이션을 통한 풀이(DP의 일종). 시간복잡도 O(N)

N = int(input())
memo = [0, 1]

for _ in range(N - 1):
  memo.append(memo[-1] + memo[-2])

print(memo[N])
