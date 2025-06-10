import sys

def main():
    # Read all input lines at once
    lines = sys.stdin.read().splitlines()
    
    # Extract values from input
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    k = int(lines[2])
    
    result = []
    for i in range(n - k + 1):
        window = arr[i:i+k]
        found = False
        for num in window:
            if num < 0:
                result.append(str(num))
                found = True
                break
        if not found:
            result.append('0')
    
    print(' '.join(result))

if __name__ == "__main__":
    main()


# cat input.txt | python solution.py