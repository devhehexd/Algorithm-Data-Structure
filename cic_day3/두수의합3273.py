import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().strip().split()))
numbers.sort()
X = int(input())

left_p = 0
right_p = N - 1
count = 0

while left_p < right_p:
  if numbers[left_p] + numbers[right_p] > X:
    right_p -= 1
    
  elif numbers[left_p] + numbers[right_p]< X:
    left_p += 1

  else:
    count += 1
    right_p -= 1
    left_p += 1

print(count)