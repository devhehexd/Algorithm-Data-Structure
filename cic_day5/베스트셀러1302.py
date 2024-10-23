import sys
sys.stdin = open("D:\Algorithm_Data_Structure\cic_day5\input1302.txt")

import sys
input = sys.stdin.readline

from collections import defaultdict

N = int(input())

book_info = defaultdict(int)

for _ in range(N):
  book = input()
  book_info[book] += 1

# 선형탐색을 이용한 방법
cnt = 0
bestseller = ""

for book_name, selling in book_info.items():
  print(book_name, selling)
  if selling > cnt:
    bestseller = book_name
    cnt = selling
  elif selling == cnt:
    bestseller = min(bestseller, book_name)

print(bestseller)

# 정렬을 이용한 방법
print(sorted(book_info.items(), key = lambda x : (-x[1], x[0]))[0][0])