class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for ele in nums:
            freq_table[ele] = freq_table.get(ele, 0) + 1
        
        print(freq_table)
        a_list = sorted(freq_table, key=freq_table.get, reverse=True)

        return a_list[:k]