class Solution(object):
    def merge(self, intervals):
        """
        overlaps when interval[x][1] <= interval[y][0]
        sort first
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda i: i[0])
        non_overlapping = [intervals[0]]

        for interval in enumerate(intervals, 1):
            start, end = interval

            last_interval = non_overlapping[-1]

            if last_interval[1] >= start:
                last_interval[0] = min(last_interval[0], start)
                last_interval[1] = max(last_interval[1], end)
            else:
                non_overlapping.append([start, end])

        return non_overlapping
