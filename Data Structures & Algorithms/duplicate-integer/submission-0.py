class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_list = []
        for n in nums:
            if n in seen_list:
                return True
            seen_list.append(n)
        return False
        