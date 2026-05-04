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
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = matrix[(top + bot) // 2]

            if row[0] <= target <= row[-1]:
                return self.binSearch(row, target)
            elif target > row[-1]:
                top = ((top + bot) // 2) + 1
            elif target < row[0]:
                bot = ((top + bot) // 2) - 1

        return False