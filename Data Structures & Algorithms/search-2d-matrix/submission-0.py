class Solution:
    def binSearch(self, row, target):
        l, r = 0, len(row) - 1

        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif target < row[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return self.binSearch(row, target)

        return False