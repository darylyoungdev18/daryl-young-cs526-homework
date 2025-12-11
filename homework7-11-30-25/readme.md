# CS526 Homework 7
**Due Date:** December 4, 2025

---

## Problem 1: Huffman Encoding and Decoding

### Key Questions Asked
- How to construct a frequency map from arbitrary text input (file or stdin) robustly?
- How to build the Huffman tree and generate prefix-free binary codes deterministically?
- How to encode the input text into a bitstring and print the frequency map and tree clearly?
- How to decode the bitstring using the code map to reconstruct the original document?
- How to handle edge cases (empty input, single unique character) without crashing?

### Algorithm Core
- Frequency Map:
  - Scan the input string and count occurrences per character using a dictionary.
- Huffman Tree:
  - Use a min-heap of nodes (char, freq).
  - Pop two minimum nodes, merge as an internal node with combined freq, push back; repeat until one root remains.
- Code Generation:
  - DFS from root; append “0” for left, “1” for right; assign codes at leaves. If the input has one unique character, assign code “0” to avoid empty code.
- Encoding:
  - Replace each character in the input with its code; concatenate to produce the encoded bitstring.
- Decoding:
  - Invert the code map (code → char); scan the bitstring incrementally, emitting a character whenever a code matches.
- I/O and Outputs:
  - Read from file path (argv[1]) or stdin.
  - Print input text, frequency map, tree (preorder with 0/1 edges), codes, and encoded bitstring to the terminal.
  - Write files: compressed.huff (bitstring), codes.json (symbol→code), reconstructed.txt (decoded text).
