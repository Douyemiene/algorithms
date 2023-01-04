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


