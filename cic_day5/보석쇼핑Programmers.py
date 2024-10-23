from collections import defaultdict

def solutions(gems):
  size = len(set(gems))
  answer=[1, len(gems)]
  
  # 투포인터 세팅
  l = r = 0
  gem_info = defaultdict(int)
  gem_info[gems[0]] += 1
  
  # 포인터 이동
  while r < len(gems): 
  # 종류가 다 있다면?
    if len(gem_info) == size:
      if r - l < answer[1] - answer[0]:
        answer = [l + 1, r + 1]
      
      gem_info[gems[l]] -= 1
      if gem_info[gems[l]] == 0:
        del gem_info[gems[l]]
      
      l += 1
      
  # 종류가 부족하다면?
    else:
      r += 1
      if r == len(gems):
        break
      gem_info[gems[r]] += 1
  
  return answer   
  