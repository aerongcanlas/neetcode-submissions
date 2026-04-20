class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_memo, t_memo = {}, {}

        for c in s:
            if c in s_memo:
                s_memo[c] += 1
            else:
                s_memo[c] = 1

        for c in t:
            if c in t_memo:
                t_memo[c] += 1
            else:
                t_memo[c] = 1

        return s_memo == t_memo