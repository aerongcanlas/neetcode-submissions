class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo_1, memo_2 = {}, {}
        
        for i in range(len(s)):
            memo_1[s[i]] = 1 + memo_1.get(s[i], 0)
            memo_2[t[i]] = 1 + memo_2.get(t[i], 0)

        return memo_1 == memo_2
