class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            frq[n] += 1

        for val, freq in frq.items():
            buckets[freq].append(val)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        



            

            