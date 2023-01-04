# Given a list of non-overlapping intervals sorted by their start time, insert a given
#  interval at the correct position and merge all necessary intervals to produce a list 
# that has only mutually exclusive intervals.

# Example 1:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# target[start] >= preceeding_interval[start] and target[start] <= next_interval[start]:
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].


# b completes overlaps a


# merge condition
# preceed_interval.end >= current.start


# [1, 3], [4, 7], []

def mergeIntervals(intervals, target):
    intervals.sort(key = lambda i: i[0])

    merged_intervals = []
    start_index, end_index = 0, 1
   
    for start, end in intervals:
        if end < target[start_index] or start > target[end_index]:
            merged_intervals.append([start, end])
        else:
            min_start = min(start, target[start_index])
            max_end = max(end, target[end_index])

            merged_intervals.append([min_start, max_end])



    return merged_intervals


def main():
  print("Intervals after inserting the new interval: " +
        str(mergeIntervals([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " +
        str(mergeIntervals([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " +
        str(mergeIntervals([[2, 3], [5, 7]], [1, 4])))


main()


