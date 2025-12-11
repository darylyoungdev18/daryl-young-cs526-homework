"""
Research and Implement a Radix Sort using human readable variable names.
You must demonstrate your code by creating your own input files with small, medium and large number of input values (e.g. 15, 50 and 500).
To show your code working, provide screen shots of your code executing printing the input values and the sorted values.
In your readme file, you must describe the heart of each algorithm and then compare and contrast their performance and when you would use them. You must provide exact directions on how to run your code.
"""
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n  # output array
    count = [0] * 10  # count array for digits (0 to 9)

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers
    for i in range(n):
        arr[i] = output[i] 
    return arr
def radix_sort(arr):
    # Find the maximum number to know number of digits
    max_num = max(arr)

    # Do counting sort for every digit. exp is 10^i where i is current digit number
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

if __name__ == "__main__":
    import sys
    from pathlib import Path

    raw_text = ""
    input_name = "stdin"
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        input_name = input_path.name
        raw_text = input_path.read_text()
    else:
        raw_text = sys.stdin.read()

    # Parse input into a list of integers
    input_numbers = [int(x) for x in raw_text.split() if x.isdigit()]

    print(f"File Input: {input_name}")
    sorted_numbers = radix_sort(input_numbers)
    print("Sorted Output:", sorted_numbers)