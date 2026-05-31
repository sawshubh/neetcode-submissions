class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            max_f = 0
            hmp = {}
            for j in range(i, len(s)):
                hmp[s[j]] = hmp.get(s[j], 0) + 1
                max_f = max(max_f, hmp[s[j]])

                if (j - i + 1) - max_f <= k:
                    res = max(res, j - i + 1)
        
        return res
