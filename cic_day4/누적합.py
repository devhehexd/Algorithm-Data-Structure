nums = [3, 5 ,1, 4, 2]

# 누적합을 구하는 3가지 방법

# 1
acc = []
sum = 0

for num in nums:
  sum += num
  acc.append(sum)

# 2
acc = [nums[0]]
for i in range(1, len(nums)):
  acc.append(acc[-1] + nums[i])

# 3
from itertools import accumulate

acc = [0] + list(accumulate(nums))