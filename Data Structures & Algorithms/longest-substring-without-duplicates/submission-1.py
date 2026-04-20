class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left, maxLen = 0,0
        for i in range(len(s)):
            if s[i] in charMap:
                left = max(charMap[s[i]]+1, left)
            charMap[s[i]] = i
            maxLen = max(maxLen, i - left + 1)

        return maxLen

