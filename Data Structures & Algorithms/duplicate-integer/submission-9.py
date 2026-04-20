class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for n in nums:
            memo.add(n)
        
        return len(memo) != len(nums)