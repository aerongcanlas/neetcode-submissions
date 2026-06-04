class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        l = 0

        while l <= len(nums) - 3:
            m, r = l + 1, len(nums) - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if total == 0:
                    res.add((nums[l], nums[m], nums[r]))
                    m, r = m+1, r-1
                elif total > 0:
                    r -= 1
                else:
                    m += 1
            l += 1

        return list(res)