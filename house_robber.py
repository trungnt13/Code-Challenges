from typing import List


def rob1(nums: List[int], index: int = 0) -> int:
  if index >= len(nums):
    return 0
  return max(nums[index] + rob1(nums, index + 2), rob1(nums, index=index + 1))


# 1. No need to try combination with 1 element
# 2. No need to try combination that is contained in bigger one
# 3. Max distance between two house is 2
#   [3 1 1 1 5] more than 2, just rob the middle one and continue
#   [3 1 1 5]

def rob2(nums: List[int]) -> int:
  pass


def rob(nums: List[int]) -> int:
  pick1, pick2 = nums[0], 0
  for n in nums[1:]:
    pick1, pick2 = pick2 + n, max(pick1, pick2)
  return max(pick1, pick2)


print(rob([2, 1, 1, 2, 1]))
print(rob1([2, 1, 1, 2, 1]))
