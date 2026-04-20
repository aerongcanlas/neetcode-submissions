class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for i, s in enumerate(strs):
            sorted_strs.append((sorted(s), i))

        sorted_strs.sort()

        cur = [strs[sorted_strs[0][1]]]
        res = []
        for i in range(1, len(sorted_strs)):
            if sorted_strs[i][0] == sorted_strs[i-1][0]:
                cur.append(strs[sorted_strs[i][1]])
            else:
                res.append(cur)
                cur = [strs[sorted_strs[i][1]]]
        if cur:
            res.append(cur)
        return res
            



        