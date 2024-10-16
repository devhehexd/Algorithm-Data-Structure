import sys
input = sys.stdin.readline

from collections import defaultdict

N = int(input())
# book_info = {}
# for _ in range(N):
#   book_name = input().strip()
#   if book_name not in book_info:
#     book_info[book_name] = 1
#   else:
#     book_info[book_name] += 1

book_info = defaultdict(int)
for _ in range(N):
  book_name = input().strip()
  
  book_info[book_name] += 1

print(book_info)