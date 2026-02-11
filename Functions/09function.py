def length_of_longest_substring(s: str):
    char_map = {}
    left = 0
    max_length = 0
    s=input("Enter a string:")
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left: # If the character is already in the map and within the current window
            left = char_map[s[right]] + 1  # Move the left pointer to the right of the previous occurrence
        
        char_map[s[right]] = right
        current_window_size = right - left + 1
        max_length = max(max_length, current_window_size)
        
    return max_length