class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if r - l == 1:
                return nums[r] if nums[r] < nums[l] else nums[l]
            
            mid = (l + r) // 2
            if nums[l] > nums[mid]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid
            else:
                return nums[l]
        return nums[l]