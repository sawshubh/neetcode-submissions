class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # common approach O(k * log n + k)
        # hash_map = {}
        # for word in strs:
        #     st_word = "".join(sorted(word))
        #     if st_word not in hash_map:
        #         hash_map[st_word] = []            
        #     hash_map[st_word].append(word)
        
        # grp_list = []
        # for k, v in hash_map.items():
        #     grp_list.append(v)
        
        # return grp_list

        hash_map = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                index = ord(c) - ord('a')
                count[index] += 1
            
            hash_map[tuple(count)].append(word)
        
        return list(hash_map.values())


        