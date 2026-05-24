class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        hash_set = set()
        nums.sort()
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0:
                    tmp = [nums[i], nums[l], nums[r]]
                    hash_set.add(tuple(tmp))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
            
        return [list(i) for i in hash_set]