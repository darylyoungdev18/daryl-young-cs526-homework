# CS526 Homework 6
**Due Date:** November 24, 2025

---

## Problem 1: Sorting and I/O (Merge/Quick/Insertion)

### Key Questions Asked
- How should the program read numbers (file path argument vs stdin) and handle missing files or empty input gracefully?
- How to normalize input with mixed spaces/newlines and ignore non-numeric tokens?
- How to present results consistently for each algorithm to verify correctness?

### Algorithm Core
- Input handling:
  - If a filename is provided as argv[1], read from that file; otherwise read from stdin.
  - Tokenize by whitespace, filter with str.isdigit(), convert to int.
- Sorting implementations:
  - Merge Sort: divide-and-conquer with merge step combining two sorted halves.
  - Quick Sort: partition around a pivot and recursively sort subarrays.
  - Insertion Sort: build sorted prefix by inserting each element into position.
- Output:
  - Print “File Input: <name>”, “Original Numbers”, then the three sorted outputs.
  - Handle empty input by printing empty lists without crashing.

---

## Problem 2: Radix Sort (Non-negative Integers)

### Key Questions Asked
- How to ensure inputs are valid for LSD radix sort (non-negative integers only)?
- How to choose base (10) and number of passes based on maximum value?
- How to perform stable bucket collection for each digit position efficiently?

### Algorithm Core
- Input handling:
  - Read from file path argument or stdin; parse whitespace-separated integers; reject negatives.
- Radix Sort (LSD):
  - Determine max digits from the largest number.
  - For each digit position (units, tens, …):
    - Place numbers into 10 buckets [0..9] based on current digit.
    - Collect buckets in order to preserve stability.
- Output:
  - Print input filename and original list, then the radix-sorted list.
  - If the input is empty, return an empty list; if any negative is detected, report an error and skip sorting.

---

## Problem 3: Gale–Shapley Stable Matching (Names-based)

### Key Questions Asked
- How to parse preference lists that use actual names rather than indexed IDs?
- How to track proposals and current engagements while comparing preferences quickly?
- How to demonstrate the matching and verify stability with the given input files?

### Algorithm Core
- Parsing:
  - Read n from the first line.
  - Build men_preferences: dict man_name -> ordered list of women’s names.
  - Build women_preferences: dict woman_name -> ordered list of men’s names.
- Matching (men-proposing Gale–Shapley):
  - Maintain free_men queue and per-man next proposal index.
  - For each proposal: if the woman is free, engage; else compare ranks and switch if she prefers the new man.
- Verification and Output:
  - Print men’s and women’s preferences and final matches (man <-> woman).
  - Optionally check for blocking pairs by rank comparison to confirm stability.# CS526 Homework 6
**Due Date:** December 10, 2025

---

## Problem 1: Sorting and I/O (Merge/Quick/Insertion)

### Key Questions Asked
- How should the program read numbers (file path argument vs stdin) and handle missing files or empty input gracefully?
- How to normalize input with mixed spaces/newlines and ignore non-numeric tokens?
- How to present results consistently for each algorithm to verify correctness?

### Algorithm Core
- Input handling:
  - If a filename is provided as argv[1], read from that file; otherwise read from stdin.
  - Tokenize by whitespace, filter with str.isdigit(), convert to int.
- Sorting implementations:
  - Merge Sort: divide-and-conquer with merge step combining two sorted halves.
  - Quick Sort: partition around a pivot and recursively sort subarrays.
  - Insertion Sort: build sorted prefix by inserting each element into position.
- Output:
  - Print “File Input: <name>”, “Original Numbers”, then the three sorted outputs.
  - Handle empty input by printing empty lists without crashing.

---

## Problem 2: Radix Sort (Non-negative Integers)

### Key Questions Asked
- How to ensure inputs are valid for LSD radix sort (non-negative integers only)?
- How to choose base (10) and number of passes based on maximum value?
- How to perform stable bucket collection for each digit position efficiently?

### Algorithm Core
- Input handling:
  - Read from file path argument or stdin; parse whitespace-separated integers; reject negatives.
- Radix Sort (LSD):
  - Determine max digits from the largest number.
  - For each digit position (units, tens, …):
    - Place numbers into 10 buckets [0..9] based on current digit.
    - Collect buckets in order to preserve stability.
- Output:
  - Print input filename and original list, then the radix-sorted list.
  - If the input is empty, return an empty list; if any negative is detected, report an error and skip sorting.

---

## Problem 3: Gale–Shapley Stable Matching (Names-based)

### Key Questions Asked
- How to parse preference lists that use actual names rather than indexed IDs?
- How to track proposals and current engagements while comparing preferences quickly?
- How to demonstrate the matching and verify stability with the given input files?

### Algorithm Core
- Parsing:
  - Read n from the first line.
  - Build men_preferences: dict man_name -> ordered list of women’s names.
  - Build women_preferences: dict woman_name -> ordered list of men’s names.
- Matching (men-proposing Gale–Shapley):
  - Maintain free_men queue and per-man next proposal index.
  - For each proposal: if the woman is free, engage; else compare ranks and switch if she prefers the new man.
- Verification and Output:
  - Print men’s and women’s preferences and final matches (man <-> woman).
  - Optionally check for blocking pairs by rank comparison to confirm stability.