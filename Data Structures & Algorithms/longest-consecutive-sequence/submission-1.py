class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # print(set(sorted(nums)))
        num_set = set(nums)
        is_consq = 0
        for i in num_set:
            streak, curr = 0, i
            while curr in num_set:
                streak += 1
                curr += 1
            is_consq = max(is_consq, streak)
        return is_consq
