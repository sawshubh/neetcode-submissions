class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean_str = ""
        # for c in s:
        #     if c.isalnum():
        #         clean_str += c.lower()
        # return clean_str == clean_str[::-1]
        
        i = 0
        j = len(s) - 1
        # print(mid)
        while i < j:
            if i < j and not s[i].isalnum():
                print("i is not alpha: idx", i, "letter: ", s[i])
                i += 1
                continue
            
            if i < j and not s[j].isalnum():
                print("j is not alpha: idx", j, "letter: ", s[j])
                j -= 1
                continue

            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True
                    
        