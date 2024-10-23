from itertools import permutations

T = int(input())

for _ in range(T):
  k= int(input())
  words = [input() for _ in range(k)]
  
  for w1, w2 in permutations(words, 2):
    p = w1 + w2
    
    if p == p[::-1]: # 회문이라면
        print(p)
        break
  
  else:
    print(0)
    
# 이중 반복문을 이용한 방법
for _ in range(T):
  k = int(input())
  words = [input() for _ in range(k)]
  
  for i in range(k):
    for j in range(k):
      if i == j:
        continue
      
      p = words[i] + words[j]
      
      if p == p[::-1]:
        print(p)
        exit(0)
  
  print(0)