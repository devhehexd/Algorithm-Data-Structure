import sys

sys.stdin = open("D:\Algorithm_Data_Structure\cic_task\input4835.txt")

input = sys.stdin.readline

T = int(input())

diff_list = []

for tc in range(T):
  N, M = list(map(int, input().split()))
  numbers = list(map(int, input().split()))
  
  section_sum = sum(numbers[:M])
  answer_list = [section_sum]
  
  for i in range(0, N - M):
      section_sum = section_sum - numbers[i] + numbers[i + M]
      answer_list.append(section_sum)
  
  max_value = max(answer_list)
  min_value = min(answer_list)

  diff = max_value - min_value
  
  diff_list.append(diff)
  
  print(f'#{tc + 1} {diff}')
  




