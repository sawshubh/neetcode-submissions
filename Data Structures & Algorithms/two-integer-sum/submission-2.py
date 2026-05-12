class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target and i != j:
                    return [i, j]
        