userInput = input()

print(userInput.rstrip(';'))

# s = "  abc123abc  "

# print(s.strip())       # ➜ "abc123abc" (removes spaces from both ends)
# print(s.rstrip())      # ➜ "  abc123abc" (removes spaces only from end)
# print(s.strip(' acb321'))  # ➜ "abc123abc" → nope, gets tricky 😄

# Use strip() when you want to clean up user input — remove all leading/trailing whitespace or special chars.
# Use rstrip() if you only want to remove characters from the end , e.g. removing newline characters or semicolons (;) at the end.
# Use lstrip() to remove indentation or prefixes.
