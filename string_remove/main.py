def remove_immediate_duplicates(s):
    result = []
    i = 0
    # print("Line:4",s)
    while i < len(s):
        # If next character is same as current, skip both
        # print("Line:7",i)
        # print("Line:8",len(s))
        if i + 1 < len(s) and s[i] == s[i + 1]:
            i += 2  # Skip both duplicates
        else:
            result.append(s[i])
            i += 1
    res_str = ''.join(result)
    return res_str if res_str else '-1'

# Test Case
userInput = input()
input_str = userInput
# input_str = "1331"
print(remove_immediate_duplicates(input_str))  # Output: 11