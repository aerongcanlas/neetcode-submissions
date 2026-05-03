class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        left = 0
        maxLen = 0

        for i in range(len(s)):
            if s[i] in indexMap:
                left = max(indexMap[s[i]] + 1, left)
            indexMap[s[i]] = i
            maxLen = max(maxLen, i-left+1)
        
        return maxLen
