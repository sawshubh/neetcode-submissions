class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force time:O(n2), space:O(1)
        # for i in range(0, len(nums)):
        #     for j in range(1, len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum == target and i != j:
        #             return [i, j]

        hash_map = {}
        for idx in range(0, len(nums)):
            diff = target - nums[idx]
            if diff in hash_map:
                return [hash_map[diff], idx]
            hash_map[nums[idx]] = idx

        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     sum = nums[l] + nums[r]
        #     if sum == target:
        #         return [l , r]
        #     elif sum < target:
        #         l += 1
        #     else:
        #         r -= 1
            


        