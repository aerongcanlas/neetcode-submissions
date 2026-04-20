class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo_1, memo_2 = {}, {}
        
        for i in range(len(s)):
            if s[i] in memo_1:
                memo_1[s[i]] += 1
            else:
                memo_1[s[i]] = 1
            if t[i] in memo_2:
                memo_2[t[i]] += 1
            else:
                memo_2[t[i]] = 1

        return memo_1 == memo_2
