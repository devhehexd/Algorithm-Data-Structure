import sys
sys.stdin = open("D:\Algorithm_Data_Structure\day8_algorithm\input1920.txt")

# ----------------------------아래로 백준 제출
import sys
input = sys.stdin.readline

N = int(input().strip())

# 정수가 저장된 리스트
number_list = list(map(int, input().strip().split()))

M = int(input().strip())

# 타겟 정수가 저장된 리스트
target_list = list(map(int, input().strip().split()))

print(number_list)
print(target_list)

import bisect

sorted_number_list = sorted(number_list)
# target들이 number_list에 존재하는가?
for target in target_list:
  index_left = bisect.bisect_left(sorted_number_list, target)
  # index_right = bisect.bisect_right(sorted_number_list, target)
  
  if index_left < len(sorted_number_list) and sorted_number_list[index_left] == target:
    print(1)
  else:
    print(0)

    
  