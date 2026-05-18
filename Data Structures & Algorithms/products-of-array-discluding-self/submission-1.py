class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        # res = []
        # for i in range(0, len(nums)):
        #     product = 1
        #     for j in range(0, len(nums)):
        #         if i == j:
        #             continue
        #         product = product * nums[j]
        #         # print(nums[i], nums[j])
        #     res.append(product)
        
        # print(res)
        # return res

        #prefix and suffix O(n)
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = [0] * n

        prefix[0] = suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]


        print(nums)
        print(prefix)
        print(suffix)
        print(res)

        return res
                