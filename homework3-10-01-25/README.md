 CS526 Homework 3


# Problem 1: Palindrome Checker (Recursion)

  The Heart of the Algorithm:
Two-Pointer Recursive Comparison
- Use recursion to compare characters from the outside moving inward
Each recursive call reduces the problem size by checking one pair of characters

Questions I asked
-How do I get the first and last characters in the strings?
-How am I going to scan the string to compare characters from one end to the next?


Algorithm Core:
```python
def is_palindrome(s, left, right):
    if left >= right: return True           # Base case: pointers met/crossed
    if s[left] != s[right]: return False    # Mismatch found
    return is_palindrome(s, left+1, right-1)  # Recurse on inner substring
```

*Why This Works:
Divide & Conquer: Break palindrome check into smaller subproblems
Early Termination: Stop immediately when mismatch found
Natural Recursion: Palindrome property is inherently recursive

---

## Problem 2: Unique Substrings Generator (Recursion)

The Heart of the Algorithm:
Systematic Enumeration with Automatic Deduplication Generate all possible substrings using nested recursion
Use Set data structure for O(1) duplicate handling

Key Questions Asked:
Outer Loop: Have we processed all starting positions? Base case for main recursion
Inner Loop: Have we generated all substrings from current position? → Base case for helper recursion
Generation: What's the next character to include in current substring? → Extend substring by one character
Uniqueness: Have we seen this substring before? → Set automatically handles this

Algorithm Core:
```python
def find_unique_substrings(s, start):
    if start >= len(s): return substrings    # All positions processed
    generate_from_position(s, start, start)   # Generate all substrings from 'start'
    return find_unique_substrings(s, start+1) # Move to next starting position

def generate_from_position(s, start, end):
    if end >= len(s): return                 # All extensions tried
    substrings.add(s[start:end+1])           # Add current substring
    generate_from_position(s, start, end+1)   # Extend by one character
```

Why This Works:
Nested Recursion: Outer recursion handles starting positions, inner handles extensions
Set Magic: Automatic duplicate elimination without manual checking
Complete Coverage: Generates every possible substring exactly once

---

## Problem 3: Stack Reversal (Multiple Data Structures)

The Heart of the Algorithm: 
Structure-Specific Recursive Reversal Strategies 
Array Stack: 
Heart:  Remove bottom element, reverse rest, place bottom on top
Key Question:  What happens when I take the bottom element out and reverse what's left?

 Linked List Stack: 
 Heart:  Reverse pointer directions recursively
Key Question:  If I reverse the tail, how do I connect the current node?

Doubly Linked List Stack: 
 Heart:  Swap next/prev pointers while traversing
 Key Question:  What becomes the new head when all pointers are swapped?

Key Questions Asked: 
Array:  How do I access the bottom element without destroying the stack structure?
Singly Linked:  How do I reverse links while maintaining reference to the new head?
Doubly Linked:  How do I swap bidirectional pointers correctly?

Algorithm Cores: 
```python
# Array: Remove bottom, reverse rest, add bottom to top
def reverse_array(stack):
    bottom = remove_bottom(stack)      # Extract bottom element
    reverse_array(stack)               # Reverse remaining elements
    stack.push(bottom)                 # Place bottom on top

# Linked List: Reverse pointer chain
def reverse_linked(head):
    if not head.next: return head      # Base case: last node is new head
    new_head = reverse_linked(head.next)  # Reverse tail
    head.next.next = head              # Reverse current link
    head.next = None                   # Break old link
    return new_head

# Doubly Linked: Swap pointers
def reverse_doubly(head):
    head.next, head.prev = head.prev, head.next  # Swap pointers
    if not head.prev: return head      # New head found
    return reverse_doubly(head.prev)   # Continue with next node
```

Why These Work: 
 Different structures require different reversal strategies 
 Recursion naturally handles the "rest of the list" problem 
 Each approach leverages the specific properties of its data structure 

---

## Problem 4: Ghostbusters Stream Crossing (Geometric Recursion)

The Heart of the Algorithm: 
 Constraint Satisfaction with Geometric Validation 
- Use backtracking to try all possible Ghostbuster-Ghost pairings
- Validate each pairing by checking if streams cross with existing pairings

Key Questions Asked: 
Assignment:  Which Ghost should this Ghostbuster target?
Validation:  Do the new stream cross any existing streams?
Feasibility:  Can the remaining Ghostbusters be assigned without conflicts?
Backtrack:  If this assignment fails, what's the next option to try?

###  Algorithm Core: 
```python
def solve_recursive(ghostbusters, ghosts, gb_index, used_ghosts, pairings):
    if gb_index == len(ghostbusters): return True    # All paired successfully
    
    for ghost_idx in range(len(ghosts)):
        if ghost_idx in used_ghosts: continue        # Ghost already used
        
        new_line = (ghostbusters[gb_index], ghosts[ghost_idx])
        
        # Critical check: Do streams cross?
        if any(lines_intersect(new_line, existing) for existing in pairings):
            continue  # Skip this pairing
        
        # Try this pairing recursively
        if solve_recursive(gb_index+1, used_ghosts | {ghost_idx}, pairings + [new_line]):
            return True
    
    return False  # No valid pairing found
```

Geometric Intersection Core: 
```python
def lines_intersect(line1, line2):
    # Heart: Cross product determines if infinite lines intersect
    (x1,y1), (x2,y2) = line1
    (x3,y3), (x4,y4) = line2
    
    dx1, dy1 = x2-x1, y2-y1    # Direction vector 1
    dx2, dy2 = x4-x3, y4-y3    # Direction vector 2
    
    cross = dx1*dy2 - dy1*dx2   # Cross product
    return abs(cross) > 1e-10   # Non-zero = intersection (not parallel)
```

Why This Works: 
 Backtracking:  Systematically explores all possibilities with early termination
 Geometric Validation:  Cross product efficiently determines line intersection
 Pruning:  Eliminates invalid branches as soon as conflict detected
 Completeness:  Guarantees finding solution if one exists

---

