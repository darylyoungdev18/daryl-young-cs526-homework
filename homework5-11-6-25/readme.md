# CS526 Homework 5
**Due Date:** November 16, 2025

---

## Problem 1: Binary Search Tree (BST)

### Key Questions Asked
- How should insert, delete, and find behave on edge cases (empty tree, leaf, single child, two children)?
- How to present the tree state so it's easy to verify correctness? (use in-order printing for sorted output)
- How to demonstrate both positive and negative findNode cases programmatically?

### Algorithm Core
- Implement Node and BST ADTs with recursive methods:
  - addNode(value): walk left/right by comparison and insert as a leaf.
  - deleteNode(value): handle three cases — no child (remove), one child (replace), two children (replace value with inorder successor and delete successor).
  - findNode(value): recursive search by value comparing to node values.
  - printTree(): in-order traversal to print sorted values.
- For demonstration: generate or load an input set, build the tree, print it, perform add/delete operations while printing after each, and run two findNode checks (one present, one absent).

---

## Problem 2: Count Vowel-Only Morse Decodings

### Key Questions Asked
- Given a continuous sequence of dots and dashes with unknown letter boundaries, which vowel Morse patterns can end at each position?
- How to accumulate counts of valid segmentations incrementally so overlapping subproblems are reused?
- How to handle noisy input files (optional leading length line, newlines, or extra characters)?

### Algorithm Core
- Predefine vowel Morse codes: A = .-, E = ., I = .., O = ---, U = ..-.
- Dynamic programming: dp[pos] = number of ways to parse the first pos symbols as vowel-only letters.
  - Initialize dp[0] = 1.
  - For each pos from 1..n, for each vowel code with length L, if the suffix morse[pos-L:pos] equals the code then dp[pos] += dp[pos-L].
- Input handling: ignore a leading integer line if present and strip all characters except '.' and '-' before running the DP.
- Output: print the input filename and dp[n] (total number of vowel-only decodings).

---

## Problem 3: Count / Construct Longest Alternating Increasing Sequence from Two Sequences

### Key Questions Asked
- How to represent states so that we maintain alternation between sequences while preserving increasing order?
- How to reconstruct the full sequence without an expensive secondary scan?
- How to choose readable state and predecessor bookkeeping to make the algorithm easy to follow and verify?

### Algorithm Core
- Use dynamic programming over prefixes of A and B. Maintain DP states that represent best lengths for sequences that end in A or end in B (or a single DP with explicit alternating-turn logic).
- When extending with an element from A, consider previous ending-in-B states whose last value is smaller; symmetrically for B.
- Store predecessor pointers (or end indices) for each DP state so the longest sequence can be reconstructed by walking pointers backward and reversing the collected elements.
- The implementation uses clear variable names and explicit backpointers to avoid a secondary while that scans again for predecessors.

---


# CS526 Homework 5
**Due Date:** November 16, 2025

---

## Problem 1: Binary Search Tree (BST)

### Key Questions Asked
- How should insert, delete, and find behave on edge cases (empty tree, leaf, single child, two children)?
- How to present the tree state so it's easy to verify correctness? (use in-order printing for sorted output)
- How to demonstrate both positive and negative findNode cases programmatically?

### Algorithm Core
- Implement Node and BST ADTs with recursive methods:
  - addNode(value): walk left/right by comparison and insert as a leaf.
  - deleteNode(value): handle three cases — no child (remove), one child (replace), two children (replace value with inorder successor and delete successor).
  - findNode(value): recursive search by value comparing to node values.
  - printTree(): in-order traversal to print sorted values.
- For demonstration: generate or load an input set, build the tree, print it, perform add/delete operations while printing after each, and run two findNode checks (one present, one absent).

---

## Problem 2: Count Vowel-Only Morse Decodings

### Key Questions Asked
- Given a continuous sequence of dots and dashes with unknown letter boundaries, which vowel Morse patterns can end at each position?
- How to accumulate counts of valid segmentations incrementally so overlapping subproblems are reused?
- How to handle noisy input files (optional leading length line, newlines, or extra characters)?

### Algorithm Core
- Predefine vowel Morse codes: A = .-, E = ., I = .., O = ---, U = ..-.
- Dynamic programming: dp[pos] = number of ways to parse the first pos symbols as vowel-only letters.
  - Initialize dp[0] = 1.
  - For each pos from 1..n, for each vowel code with length L, if the suffix morse[pos-L:pos] equals the code then dp[pos] += dp[pos-L].
- Input handling: ignore a leading integer line if present and strip all characters except '.' and '-' before running the DP.
- Output: print the input filename and dp[n] (total number of vowel-only decodings).

---

## Problem 3: Count / Construct Longest Alternating Increasing Sequence from Two Sequences

### Key Questions Asked
- How to represent states so that we maintain alternation between sequences while preserving increasing order?
- How to reconstruct the full sequence without an expensive secondary scan?
- How to choose readable state and predecessor bookkeeping to make the algorithm easy to follow and verify?

### Algorithm Core
- Use dynamic programming over prefixes of A and B. Maintain DP states that represent best lengths for sequences that end in A or end in B (or a single DP with explicit alternating-turn logic).
- When extending with an element from A, consider previous ending-in-B states whose last value is smaller; symmetrically for B.
- Store predecessor pointers (or end indices) for each DP state so the longest sequence can be reconstructed by walking pointers backward and reversing the collected elements.
- The implementation uses clear variable names and explicit backpointers to avoid a secondary while that scans again for predecessors.

---
