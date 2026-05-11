class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_hash = {}
        t_hash = {}

        for s_ele, t_ele in zip(s, t):
            s_hash[s_ele] = s_hash.get(s_ele, 0) + 1
            t_hash[t_ele] = t_hash.get(t_ele, 0) + 1

        for k, v in s_hash.items(): 
            if v != t_hash.get(k, 0):
                return False
        return True

        
            