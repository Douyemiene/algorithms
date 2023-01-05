class Solution(object):
    def insert(self, intervals, target):
        intervals.sort(key=lambda i: i[0])

        merged_intervals = []
        start_index, end_index = 0, 1
        last_index = len(intervals) - 1
        count = -1

        if len(intervals) == 0:
            return [target]

        for index, interval in enumerate(intervals):
            start, end = interval
            interval_overlaps_target = start <= target[end_index]

            if end < target[start_index]:
                merged_intervals.append([start, end])

                if index == last_index:
                    merged_intervals.append(target)
            elif interval_overlaps_target:
                min_start = min(start, target[start_index])
                max_end = max(end, target[end_index])
                target = [min_start, max_end]

                if index == last_index:
                    merged_intervals.append(target)
            else:
                count += 1
                if count == 0:
                    merged_intervals.append(target)
                merged_intervals.append([start, end])

        return merged_intervals

        return merged_intervals
