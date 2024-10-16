import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())

book_info = [input().strip() for _ in range(N)]
book_info = Counter(book_info)

print(book_info)