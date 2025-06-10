userInput = input()

def remove_duplicates(s):
    # Step 1: Count occurrences of each character
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    # Step 2: Build result string with characters appearing exactly once
    result = ''.join([char for char in s if count[char] == 1])

    return result

# Function call and output
print(remove_duplicates(userInput))