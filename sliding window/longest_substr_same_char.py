def longest_substr_same_char(_str, k):
    window_start = 0 
    char_map = {}
    maxFreq = 0
    longest_substr_same_char = 0 

    for window_end, char in enumerate(_str):
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    
        maxFreq = max(list(char_map.values()))  
        no_chars_in_window = window_end - window_start + 1  

        while no_chars_in_window - maxFreq > k: 
            charAtStart = _str[window_start]
            char_map[charAtStart] -= 1
            window_start += 1
            no_chars_in_window = window_end - window_start + 1  

            if char_map[charAtStart] == 0:
                del char_map[charAtStart]

    
    no_in_window = window_end - window_start + 1  
    longest_substr_same_char = max(no_in_window, longest_substr_same_char)
    
    return longest_substr_same_char


print(longest_substr_same_char("abccde", 1))