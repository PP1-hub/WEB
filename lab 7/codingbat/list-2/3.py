def centered_average(nums):
  sum = 0
  small = min(nums)
  big = max(nums)

  for i in range(len(nums)):
     sum += nums[i]

  return (sum - small - big) / (len(nums) - 2)
