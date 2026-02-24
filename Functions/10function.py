def reverse_string(s):
    return s[::-1]
text = "hello"
reversed_text = reverse_string(text)
print(reversed_text)  # Output: "olleh"

# else
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str