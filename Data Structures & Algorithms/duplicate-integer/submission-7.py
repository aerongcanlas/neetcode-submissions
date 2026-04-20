class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for n in nums:
            if n in memo:
                return True
            memo[n] = 1
        
        return False