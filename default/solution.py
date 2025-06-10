# cat input.txt | python solution.py

import sys

def main():
    # Read all input lines at once
    lines = sys.stdin.read().splitlines()
    
    # Extract values from input
    # print(lines)

    def is_balanced(s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return 0
            else:
                pass  # ignore characters that are not parentheses
        return 1 if not stack else 0
        
    # Sample Input
    print(is_balanced(lines[0]))

if __name__ == "__main__":
    main()


