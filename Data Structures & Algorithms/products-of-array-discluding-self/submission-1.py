class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward, reverse = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            forward[i] = forward[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            reverse[i] = reverse[i+1] * nums[i+1]

        for i in range(len(nums)):
            nums[i] = forward[i] * reverse[i]

        return nums
