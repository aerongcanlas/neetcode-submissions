class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        memo = {}
        res = 1
        nums.sort()
        for n in nums:
            if n - 1 in memo:
                memo[n] = memo[n-1] + 1
                res = max(memo[n], res) 
            else:
                memo[n] = 1
        
        return res