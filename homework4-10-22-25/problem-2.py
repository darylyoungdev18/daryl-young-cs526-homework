# the algorithm below sorts the numbers array from greatest to smallest
#the from there each number is added to total and compared to target.

def smallest_number_elements(num, target):
    num.sort(reverse= True)
    total = 0 
    count = 0
    for n in num:
        total += n
        count += 1
        if total >= target:
            return count
        


def parse_value(val_str):
    """
    Try to parse as int first, if it fails try float
    """
    try:
        return int(val_str)
    except ValueError:
        try:
            return float(val_str)
        except ValueError:
            return val_str

def main():
    """
    Main function with standard input/output
    
    Input format:
    Line 1: Array of numbers (space-separated)
    Line 2: Target value
    
    Example 1:
    5 10 2 8 3
    15
    
    Example 2:
    1 2 3 4 5 6 7 8 9 10
    25
    
    Example 3:
    100 50 25 10 5
    200
    """
    try:
        # Read array of numbers
        numbers_input = input().strip().split()
        numbers = [parse_value(x) for x in numbers_input]
        
        # Read target value
        target = parse_value(input().strip())
        
        print(f"Numbers: {numbers}")
        print(f"Target: {target}")
        
        # Find smallest number of elements
        result = smallest_number_elements(numbers.copy(), target)
        
        if result == -1:
            print(f"\nResult: Cannot reach target {target} with given numbers")
        else:
            print(f"\nResult: {result} element(s) needed to reach target {target}")
            
            # Show which elements were used (for verification)
            sorted_nums = sorted(numbers, reverse=True)
            selected = sorted_nums[:result]
            print(f"Elements used: {selected}")
            print(f"Sum: {sum(selected)}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()