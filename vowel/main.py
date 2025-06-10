#Getting input via STDIN
userInput = input()

vowels=["a","e","i","o","u"]

def isVowel(str):
    for char in str:
        # print(char)
        if char.lower() in vowels:
            return True
    return False

if isVowel(userInput):
    print("yes")
else:
    print("no")