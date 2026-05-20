class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # print(set(sorted(nums)))
        # num_set = set(nums)
        # is_consq = 0
        # for i in num_set:
        #     streak, curr = 0, i
        #     while curr in num_set:
        #         streak += 1
        #         curr += 1
        #     is_consq = max(is_consq, streak)
        # return is_consq

        longest = 0
        num_set = set(nums)

        for num in nums:
            if (num -  1) not in num_set:
                length = 1
                print("num: ", num, " lenght: ", length, " sum: ", num + length)
                while(num + length) in num_set:
                    length = length + 1
                longest = max(length, longest)
        
        return longest
