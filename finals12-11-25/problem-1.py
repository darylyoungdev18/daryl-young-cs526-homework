"""
Save the village from flooding! The dam is weakening! You are the only person with the skills to fix cracks in the dam. Cracks of different sizes appear at different times. Every time unit they remain unfixed, they get a little larger. You can work fast enough to fix one crack every time unit. Each time unit, the ground in the village can absorb some of the incoming water, but if the total floodwaters reach or exceed a certain level, the village must be evacuated. 
Input specification: the first line contains the integer n, representing the number of cracks that occur in the dam. 
The second line contains a positive integer indicating the threshold (units of water) for how much flooding the village can withstand before having to evacuate. If the floodwaters equal or exceed this threshold, the village is considered flooded and must be evacuated. 
The third line contains a positive integer indicating the amount (units of water) that drain out of the village each time unit. 
Following that are n lines. Each line contains 2 values, separated by a space, that specify a particular crack. The first value on a line indicates the time unit that the crack appears. This value is guaranteed to be a non-negative integer. The second value on the line indicates the initial size associated with this crack. This value is guaranteed to be a positive integer. It represents the number of units of water that can flow through it in one time unit. You may assume that n is not bigger than 1,000,000 and that each input value fits in a 32-bit integer. You may also assume that the input file lists the cracks in non-decreasing order of time of appearance.

You are able to fix one crack per time unit, and can choose to fix a crack in the same time unit that it appears, or delay it for a later time unit. Note that there may be multiple cracks that appear at the same time unit. (The problem is trivial if this doesn't occur.) At the end of a time unit, all remaining,
unfixed cracks increase in size by one.
To simplify, we will discretize these continuous processes as follows. In time unit t:
All new cracks that appear in time unit t appear at the beginning of the time unit.
You are able to instantaneously fix one crack that appeared at time unit t, or that appeared earlier but was not fixed yet.
The floodwaters in the village are adjusted in a single calculation, that adds floodwater according to the total size of all the current, unfixed
cracks, and decreases floodwater according to the amount that can be drained in one time unit. The floodwaters can never go below zero (you
can't drain water that isn't present). If the floodwaters ever equal or exceed the threshold, the village is flooded and must be evacuated at that
point.
Finally, all of the remaining cracks increase in size by 1. This essentially happens all at once as the current time unit ends.
Output specification: to help with debugging, the output includes a couple of pieces of information. If flooding occurs, the output contains three lines
of information. The first line is the word "FLOOD". The second line contains an integer indicating which time unit resulted in flooding. The third line
indicates the total units of floodwater present when flooding occurred. If flooding does not occur, the output contains two lines of information. The
first line is the word "SAFE". The second line contains an integer indicating the maximum value the floodwaters ever reached.
You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how to run your code and you must submit screen shots of your running code on all provided inputs and printing your result to the console

Sample input file:
2
10
3
0 7
0 8

Output:
python3 flood.py < flood_inputs/flood_1.txt 
SAFE
4

"""
import sys
from pathlib import Path
import heapq
class Crack:
    def __init__(self, appearance_time: int, initial_size: int):
        self.appearance_time = appearance_time
        self.initial_size = initial_size

    def size_at_time(self, current_time: int) -> int:
        """Calculate the size of the crack at a given time."""
        return self.initial_size + (current_time - self.appearance_time)
    
def simulate_flood(cracks, threshold, drain_amount):
    flood_water = 0
    max_flood_water = 0
    current_time = 0
    crack_index = 0
    n = len(cracks)

    min_heap = []  # (base_size, tie_breaker, crack)
    tie_counter = 0
    size_offset = 0
    sum_base_sizes = 0

    while crack_index < n or min_heap:
        # If heap is empty and next crack is in the future, fast-forward time
        if not min_heap and crack_index < n and cracks[crack_index].appearance_time > current_time:
            current_time = cracks[crack_index].appearance_time
            # no cracks yet, so no floodwater gained; continue to add new cracks
            # (skip per-tick drain/growth because nothing exists to drain/grow)

        # Add all cracks that appear at current_time
        while crack_index < n and cracks[crack_index].appearance_time == current_time:
            c = cracks[crack_index]
            base_size = c.initial_size
            heapq.heappush(min_heap, (base_size, tie_counter, c))
            tie_counter += 1
            sum_base_sizes += base_size
            crack_index += 1

        # Fix one smallest crack if available
        if min_heap:
            base_size, _, _ = heapq.heappop(min_heap)
            sum_base_sizes -= base_size

        # Compute floodwater contribution this tick (only if any cracks exist)
        total_crack_size = sum_base_sizes + len(min_heap) * size_offset
        flood_water += total_crack_size

        # Drain
        flood_water = max(0, flood_water - drain_amount)

        # Flood check
        if flood_water >= threshold:
            print("FLOOD")
            print(current_time)
            print(flood_water)
            return

        max_flood_water = max(max_flood_water, flood_water)

        # Growth happens only when there are remaining cracks
        if min_heap:
            size_offset += 1

        current_time += 1

    print("SAFE")
    print(max_flood_water)

if __name__ == "__main__":
    raw_text = ""
    input_name = "stdin"
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        input_name = input_path.name
        raw_text = input_path.read_text()
    else:
        raw_text = sys.stdin.read()

    lines = raw_text.splitlines()
    if len(lines) < 3:
        print("Insufficient input data.")
        sys.exit(1)

    n = int(lines[0].strip())
    threshold = int(lines[1].strip())
    drain_amount = int(lines[2].strip())

    cracks = []
    for i in range(3, 3 + n):
        appearance_time, initial_size = map(int, lines[i].strip().split())
        cracks.append(Crack(appearance_time, initial_size))

    simulate_flood(cracks, threshold, drain_amount)