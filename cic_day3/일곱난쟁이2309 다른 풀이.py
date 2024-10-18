import sys
input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]
sum_dwarfs = sum(dwarfs)

def find_spy():
  for i in range(8):
    for j in range(i + 1, 9):
      if sum_dwarfs - dwarfs[i] - dwarfs[j] == 100:
        dwarfs.pop(i)
        dwarfs.pop(j - 1)
        return


for dwarf in sorted(dwarfs):
  print(dwarfs)
