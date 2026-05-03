class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        left, maxLen = 0, 0
        for i in range(len(s)):
            if s[i] in indexMap:
                left = max(indexMap[s[i]]+1, left)
            maxLen = max(maxLen, i-left+1)
            indexMap[s[i]] = i
        
        return maxLen

