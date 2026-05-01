class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        res = set()

        while l < len(nums)-2:
            m, r = l + 1, len(nums)-1
            while m < r:
                curSum = nums[l] + nums[m] + nums[r]
                if curSum == 0:
                    res.add((nums[l], nums[m], nums[r]))
                    m += 1
                    r -= 1
                elif curSum > 0:
                    r -= 1
                else:
                    m += 1
            l += 1
        
        return [list(r) for r in res]