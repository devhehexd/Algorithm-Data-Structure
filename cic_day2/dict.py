info = {}

for _ in range(5):
  vote = input()
  if vote not in info:
    info[vote] = 1
  else:
    info[vote] += 1

print(info)