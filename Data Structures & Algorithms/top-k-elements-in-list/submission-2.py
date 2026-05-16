class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq_table = {}
        # for ele in nums:
        #     freq_table[ele] = freq_table.get(ele, 0) + 1
        
        # print(freq_table)
        # a_list = sorted(freq_table, key=freq_table.get, reverse=True)

        # return a_list[:k]

        # efficient solution
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res