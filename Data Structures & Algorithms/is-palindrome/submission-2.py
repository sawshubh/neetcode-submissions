class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for c in s:
            if c.isalnum():
                clean_str += c.lower()
        return clean_str == clean_str[::-1]
        
        # i = 0
        # j = len(s) - 1
        # mid = (len(s) - 1) // 2
        # # print(mid)
        # while j > 0:
        #     if not s[i].isalpha():
        #         print("i is not alpha: idx", i, "letter: ", s[i])
        #         i += 1
        #         continue
            
        #     if not s[j].isalpha():
        #         print("j is not alpha: idx", j, "letter: ", s[j])
        #         j -= 1
        #         continue

            
        #     if i == j and ((i + 1) == mid and (j - 1) == mid):
        #         return True
        #     else:
        #         i += 1
        #         j -= 1
            

        
        # return False
                    
        