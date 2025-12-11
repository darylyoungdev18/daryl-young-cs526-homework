"""
Implement  the Following Sorting Algorithms
Merge Sort
Quick Sort
Insertion Sort

You must demonstrate your code by creating your own input files with small, medium and large number of input values (e.g. 15, 50 and 500).
To show your code working, provide screen shots of your code executing printing the input values and the sorted values.
In your readme file, you must describe the heart of each algorithm and then compare and contrast their performance and when you would use them. You must provide exact directions on how to run your code
"""
#implement the merge sort algorithm using human readable variables names
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves/ beginning to mid
        right_half = arr[mid:] # this is mid to end

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
# Insertion Sort with human readable variable names
def insertion_sort(arr):
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index - 1

        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1

        arr[position + 1] = current_value
    return arr

#read input from a file and sort it using the three algorithms
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

    # Process input into a list of integers
    input_numbers = [int(x) for x in raw_text.split() if x.isdigit()]

    print(f"File Input: {input_name}")
    print(f"Original Numbers: {input_numbers}")

    # Merge Sort
    merge_sorted = merge_sort(input_numbers.copy())
    print(f"Merge Sorted: {merge_sorted}")

    # Quick Sort
    quick_sorted = quick_sort(input_numbers.copy())
    print(f"Quick Sorted: {quick_sorted}")

    # Insertion Sort
    insertion_sorted = insertion_sort(input_numbers.copy())
    print(f"Insertion Sorted: {insertion_sorted}")