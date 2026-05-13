class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            st_word = "".join(sorted(word))
            if st_word not in hash_map:
                hash_map[st_word] = []            
            hash_map[st_word].append(word)
        
        grp_list = []
        for k, v in hash_map.items():
            grp_list.append(v)
        
        return grp_list


        