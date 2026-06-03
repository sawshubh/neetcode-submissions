class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # target = Counter(t)
        # print(target)

        # min_len = float('inf')
        # result = ""

        # for i in range(len(s)):
        #     for j in range(i, len(s)):

        #         window = s[i:j+1]
        #         window_count = Counter(window)
        #         # print("window_count: ", window_count)

        #         valid = True

        #         for ch in target:
        #             if window_count[ch] < target[ch]:
        #                 valid = False
        #                 break

        #         if valid:
        #             if len(window) < min_len:
        #                 min_len = len(window)
        #                 result = window

        # return result
        # if t == "":
        #     return ""

        # countT, window = {}, {}
        # for c in t:
        #     countT[c] = 1 + countT.get(c, 0)

        # have, need = 0, len(countT)
        # res, resLen = [-1, -1], float("infinity")
        # l = 0
        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = 1 + window.get(c, 0)

        #     if c in countT and window[c] == countT[c]:
        #         have += 1

        #     while have == need:
        #         if (r - l + 1) < resLen:
        #             res = [l, r]
        #             resLen = r - l + 1

        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         l += 1
        # l, r = res
        # return s[l : r + 1] if resLen != float("infinity") else ""

        map_s = [0] * 256
        map_t = [0] * 256

        for ch in t:
            map_t[ord(ch)] += 1

        left = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            map_s[ord(s[right])] += 1

            while self.contains(map_s, map_t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                map_s[ord(s[left])] -= 1
                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]


    def contains(self, map_s, map_t):
        for i in range(256):
            if map_t[i] > map_s[i]:
                return False
        return True



