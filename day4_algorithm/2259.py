import sys

sys.stdin = open("./day4_algorithm/input.txt")


N, K = list(map(int, input().split()))
numbers = list(map(int, input().split()))


# 슬라이딩 윈도우를 위한 첫 구간의 합
split_sum1 = sum(numbers[:K])
# print(split_sum1)

# 모든 구간 합을 리스트에 저장 후 max 함수 사용
# 첫 번째 구간 합도 저장해야 한다
answer_list = [split_sum1]

# 기준 위치 i를 순회할 반복문
# 0 -> N - K
for i in range(0, N - K):
  # print(i)
  split_sum1 = split_sum1 - numbers[i] + numbers[i + K]
  # print(split_sum1)
  answer_list.append(split_sum1)

# 리스트에 저장된 원소 중 가장 큰 값을 출력
print(max(answer_list))