# cat input.txt | python solution.py

import sys

def main():
    # Read all input lines at once
    lines = sys.stdin.read().splitlines()
    
    # Extract values from input
    print(lines)

    

if __name__ == "__main__":
    main()


