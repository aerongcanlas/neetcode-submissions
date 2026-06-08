"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        heap = []
        for interval in intervals:
            if heap == [] or heap[0] > interval.start:
                heapq.heappush(heap, interval.end)
            else:
                heapq.heapreplace(heap, interval.end)

        return len(heap)