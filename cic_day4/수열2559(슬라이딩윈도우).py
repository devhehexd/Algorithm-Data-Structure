N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 세팅(첫 구간의 합 구하기)
max_sum = sum(nums[:M])

# 반복문(0 ~ N - M -1)
for i in range(N - M):
  tmp_sum = max_sum - nums[i] + nums[i + M]

# 갱신
  max_sum = max(max_sum, tmp_sum)
  
print(max_sum)


# 단순히 특정한 구간의 합만이 필요하거나, 계속해서 구간의 크기가 달라지는 조건의 경우 슬라이딩 윈도우는 효율적이지 않다
