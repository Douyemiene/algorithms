def max_distinct_chars(theStr, k):
    window_start = 0
    max_distinct_count = 0
    window = {}

    for window_end, char in enumerate(theStr):
        if char in window:
            window[char] += 1
        else:
            window[char] = 1



        while len(window) > k:
            charAtStart = theStr[window_start]
            window[charAtStart] -= 1

            if window[charAtStart] == 0:
                del window[charAtStart]
            window_start += 1

   
        new_distinct_count = window_end - window_start + 1
        max_distinct_count = max(max_distinct_count, new_distinct_count)

    return max_distinct_count

print(max_distinct_chars("araaci", 2))    

