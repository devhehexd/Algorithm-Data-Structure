import sys
sys.stdin = open("./day5_algorithm/input9012.txt")

import sys
input = sys.stdin.readline

# 테스트 케이스의 수
T = int(input())


for _ in range(T):
  
  # 괄호 문자열 입력
  string = input()
  
  # 스택
  stack = list()
  
  # flag 변수
  flag = False
  
  # 문자열 순회
  for char in string:
    # char가 ( 이냐
    if char == '(':
      # 스택에 저장한다.
      stack.append(char)
      
    # char가 ) 이냐
    elif char == ')':
      # 스택에 ( 있는지? 없는지?
      
      # 스택에 ( 있다면 (stack[-1]: 음수 인덱스는 거꾸로 세는 것. 즉 -1은 마지막 인덱스, -2는 마지막의 앞 ..........
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      # 스택에 ( 없다면
      else:
        # 비정상적인 문자열
        flag = True
  
  if flag == True or len(stack) != 0:
    print("NO")
  else:
    print("YES")
