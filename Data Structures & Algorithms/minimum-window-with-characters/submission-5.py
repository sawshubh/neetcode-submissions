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
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
