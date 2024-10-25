#빈 이차원 리스트 제작
matrix = [[0] * 4 for _ in range(3)]

# 입력 받기
# matrix = [list(map(int, input().split())) for _ in range(3)]

# 전치
matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]

# 반복문을 통한 구현
for r in range(3):
  for c in range(3):
    if c > r:
      matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
      
# zip 함수를 통한 구현
# 원소가 튜플이 됨
transposed_matrix = list(zip(*matrix))

# 원소를 리스트로 활용하고 싶다면 map 함수와 list 함수를 이용하여 형 변환
transposed_matrix = list(map(list, zip(*matrix)))


