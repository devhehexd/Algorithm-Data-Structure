def solution(s):
    answer = ''
    
    # 문자열 개수 저장 딕셔너리
    dic = dict()
    
    # 문자열 순회
    
    for c in s:
      if c not in dic.keys():
        dic[c] = 1
      elif c in dic.keys():
        dic[c] = dic[c] + 1
    