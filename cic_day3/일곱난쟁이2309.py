import sys
input = sys.stdin.readline

from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]

for this_case in combinations(dwarfs, 7):
  if sum(this_case) == 100:
    for dwarf in sorted(this_case):
      print(dwarf)
    
    break

