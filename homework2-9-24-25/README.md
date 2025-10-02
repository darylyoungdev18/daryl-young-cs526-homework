# Sum of Three Middle Nodes (Doubly Linked List)

This project contains a Python implementation of a recursive function that finds the sum of the three middle nodes in a doubly linked list of sorted integers.  
The list is guaranteed to have an **odd length**.

## Problem Statement
Given a doubly linked list of sorted integers with odd length, return the sum of the three middle nodes.  


## Approach
- A recursive **slow/fast pointer method** is used to find the middle node:
  - Slow pointer moves 1 step per recursion.
  - Fast pointer moves 2 steps per recursion.
  - When the fast pointer reaches the end, the slow pointer is at the middle.
- Once the middle node is found, we access its `prev` and `next` to calculate the sum.


## Usage for prbblem-4.py
### Run with stdin
You can pass a sequence of integers (space-separated) via standard input