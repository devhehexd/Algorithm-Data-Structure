# 인접 행렬 방식

V = int(input())
E = int(input())

# 1. 빈 판 만들기(V*V)
adj_matrix = [[0] * V for _ in range(V)]

# 2. 간선 정보 입력 받기(E)
for _ in range(E):
  s, e = map(int(int, input().split()))
  adj_matrix[s][e] = 1
  # 양방향 그래프일 경우 adj_matrx[e][s] = 1 추가

print(adj_matrix)


# 인접 리스트 방식
V = int(input())
E = int(input())

# 1. 빈 판 만들기
adj_list = [[] for _ in range(V)]

# 2. 간선 정보 입력 받기
for _ in range(E):
  s, e = map(int, input().split())
  adj_list[s].append(e)
  # 양방향 그래프일 경우 adj_list[e].append(s)

print(adj_list)