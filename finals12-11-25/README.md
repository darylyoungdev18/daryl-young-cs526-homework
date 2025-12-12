# CS526 Finals
**Due Date:** December 11, 2025

---

## Problem 1: Dam Breaking

### Key Questions Asked
- How to model crack arrivals and growth per time unit while fixing one crack each tick?
- How to avoid heap comparison errors when crack sizes tie?
- How to handle large inputs efficiently (fast-forward empty periods; avoid per-tick heap rebuild)?
- What outputs must be printed for FLOOD vs SAFE cases?

### Algorithm Core
- Input parsing:
  - Read n, threshold, drain_amount, then n lines of “appearance_time initial_size” in non-decreasing appearance order.
- Priority scheduling:
  - Use a min-heap keyed by base_size with a tie-breaker counter to avoid comparing objects.
  - Maintain a global size_offset representing uniform +1 growth per tick for all unfixed cracks, preserving heap order.
  - Track sum_base_sizes to compute the total crack size quickly: total = sum_base_sizes + len(heap) * size_offset.
- Simulation loop:
  - Fast-forward current_time to next crack’s appearance when heap is empty.
  - At each time unit: add new cracks, fix one smallest crack (heap pop), add floodwater from remaining cracks, drain, check threshold, and apply growth via size_offset++.
- Output:
  - FLOOD: print “FLOOD”, the time unit, and the floodwater amount at flooding.
  - SAFE: print “SAFE” and the maximum floodwater observed.


---

## Problem 2: Downhill Skier

### Key Questions Asked
- How to explore downhill moves in 8 directions while ensuring strictly decreasing altitude?
- How to avoid recomputation for overlapping subproblems on large grids?
- How to parse the matrix format and handle recursion depth safely?

### Algorithm Core
- Input parsing:
  - Read m (rows) and n (cols), then m lines of space-separated altitudes.
- DFS + memoization:
  - For each cell, DFS over up to 8 neighbors with lower altitude and compute longest path length starting there.
  - Cache results in a memo dict keyed by (x, y) to avoid rework; overall O(m*n).
- Aggregation:
  - Evaluate longest_path_from_cell for all cells and return the maximum path length.
- Output:
  - Print the single integer: length of the longest downhill path.
