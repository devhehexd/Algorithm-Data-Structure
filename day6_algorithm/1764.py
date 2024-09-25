import sys

sys.stdin = open("./day6_algorithm/input1764.txt")

"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

"""
import sys

# input 함수 코드를 readline 코드로 대체
input = sys.stdin.readline

# 공백을 기준으로 입력되느 2개의 정수
# strip() 문자열 양쪽의 공백, 개행문자를 제거
# N, M = map(int, sys.stdin.readline().strip().split())
N, M = map(int, input().strip().split())

# 듣도 못한 이름을 저장할 집합
name_set = set()

# 듣도 못한 이름 입력 반복문
for _ in range(N):
  name = input().strip()
  name_set.add(name)

name_list = []

# 보도 못한 이름 입력 반복문
for _ in range(M):
  name = input().strip()
  
  # 듣도 보도 못한 이름 목록에서 탐색
  if name in name_set:
    name_list.append(name)

count = len(name_list)

# sorted(): 정렬된 '리스트'를 '반환(생성)'
sorted_list = sorted(name_list)
print(count)
for i in sorted_list:
  print(i)