"""
    Returns the length of the longest substring
    without repeating characters.
    """


def length_of_longest_substring(s: str) -> int:
    
    char_index = {}      # Stores last seen index of each character
    left = 0             # Left pointer of sliding window
    max_length = 0       # Maximum length found
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:   # If character seen before and inside current window
            left = char_index[s[right]] + 1
        char_index[s[right]] = right # Update last seen index
        
        window_length = right - left + 1  # Calculate current window size
        max_length = max(max_length, window_length)
    
    return max_length

user_input = input("Enter a string: ")
result = length_of_longest_substring(user_input)
print("Length of longest substring:", result)

    