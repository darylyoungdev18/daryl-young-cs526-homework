# CS526 Midterm Exam


---

## Problem 1: Snowfall Analysis (Array Processing)

### **The Heart of the Algorithm:**
**Sliding Window with Cumulative Difference**
- Use cumulative snowfall array to quickly calculate any range sum
- Check every consecutive 3-day window against half of total snowfall
- Leverage cumulative property: `snowfall[i] - snowfall[i-3]` gives 3-day total

### **Key Questions Asked:**
1. **How do I calculate snowfall for any 3 consecutive days?**

2. **What if there are fewer than 3 days?**

3. **How do I compare against "more than half"?**

### **Algorithm Core:**
```python
def has_three_day_snowfall_exceeding_half(cumulative_snowfall):
    n = len(cumulative_snowfall)
    
    if n < 3:
        return "NO"
    
    total_snowfall = cumulative_snowfall[-1]
    half_total = total_snowfall / 2
    
    # Check each possible 3-day window
    for i in range(2, n):
        three_day_snowfall = cumulative_snowfall[i] - cumulative_snowfall[i - 3]
        if three_day_snowfall > half_total:
            return "YES"
    
    return "NO"
```

### **Why This Works:**
- **Cumulative Array Property:** Difference between two indices gives range sum
- **Efficient:** O(n) time complexity - single pass through array
- **Edge Cases:** Handles arrays with fewer than 3 days correctly

---

## Problem 2: Virus Spread Simulation (Grid + BFS)

### **The Heart of the Algorithm:**
**Day-by-Day Infection Simulation**
- Model state as 2D grid (0 = healthy, 1 = infected)
- Each day, check every healthy county for ≥2 infected neighbors
- Repeat until no new infections occur (steady state reached)
- Check if any healthy counties remain

### **Key Questions Asked:**
1. **How do I represent the grid state?**

2. **How do I count infected neighbors?**

3. **When does the simulation stop?**

4. **How do I avoid simultaneous update conflicts?**

### **Algorithm Core:**
```python
def are_there_healthy_counties_after_infection(n, infected_coords):
    # Initialize grid
    grid = [[0 for i in range(n)] for j in range(n)]
    
    # Mark initially infected counties
    for x, y in infected_coords:
        grid[x][y] = 1
    
    # Helper function to count infected neighbors
    def count_infected_neighbors(x, y):
        infected_count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1:
                    infected_count += 1
        return infected_count
    
    # Simulate infection spread day by day
    infection_spread = True
    while infection_spread:
        infection_spread = False
        new_infections = []
        
        # Check each healthy county
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:  # Healthy county
                    if count_infected_neighbors(i, j) >= 2:
                        new_infections.append((i, j))
        
        # Apply new infections
        for x, y in new_infections:
            grid[x][y] = 1
            infection_spread = True
    
    # Check for remaining healthy counties
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return True
    return False
```

### **Why This Works:**
- **Simulation Approach:** Models real-world day-by-day spread
- **Correct State Management:** Batch updates prevent double-counting
- **Termination Guarantee:** Finite grid ensures simulation eventually stops
- **Complete Coverage:** Checks all counties for remaining healthy ones

---

## Problem 3: Shopping Cart Optimization (Two-Pointer/Sliding Window)

### **The Heart of the Algorithm:**
**Greedy Collection with Two-Basket Constraint**
- Use a set to track which categories are currently in baskets
- Iterate through aisles from left to right
- Accept items if category already in baskets OR if we have free basket space
- Stop when encountering a third category

### **Key Questions Asked:**
1. **How do I track which categories are in my baskets?**

2. **When can I add an item?**

3. **When must I stop shopping?**

### **Algorithm Core:**
```python
def max_items_selected(aisles):
    if not aisles:
        return 0

    basket = set()  # Track categories in baskets (max 2)
    count = 0

    for category in aisles:
        # Can add if: already have this category OR baskets not full
        if category in basket or len(basket) < 2:
            basket.add(category)
            count += 1
        else:
            # Third category encountered - must stop
            break

    return count
```

### **Why This Works:**
- **Greedy Property:** Taking items as early as possible maximizes count
- **Set Efficiency:** O(1) lookup and insertion for category checking
- **Simple Logic:** Clear stopping condition prevents over-collection
- **Optimal:** Can't do better than taking all items until forced to stop


---

## Problem 4: Sudoku-like Validation (Set-based Constraint Checking)

### **The Heart of the Algorithm:**
**Triple Constraint Validation**
- Check rows: Each symbol appears at most once per row
- Check columns: Each symbol appears at most once per column
- Check sub-boards: Each symbol appears at most once per √n × √n region
- Use sets for O(1) duplicate detection

### **Key Questions Asked:**
1. **How do I check rows and columns efficiently?**

2. **How do I identify sub-boards?**

3. **How do I handle empty cells?**


### **Algorithm Core:**
```python
def is_valid_puzzle_board(board, symbols):
    n = len(board)
    sub_board_size = int(n**0.5)
    
    # Check rows and columns
    for i in range(n):
        row_symbols = set()
        col_symbols = set()
        
        for j in range(n):
            # Check row
            if board[i][j] != '.':
                if board[i][j] in row_symbols:
                    return False
                row_symbols.add(board[i][j])
            
            # Check column
            if board[j][i] != '.':
                if board[j][i] in col_symbols:
                    return False
                col_symbols.add(board[j][i])
    
    # Check sub-boards
    for row in range(0, n, sub_board_size):
        for col in range(0, n, sub_board_size):
            sub_board_symbols = set()
            for i in range(sub_board_size):
                for j in range(sub_board_size):
                    cell_value = board[row + i][col + j]
                    if cell_value != '.':
                        if cell_value in sub_board_symbols:
                            return False
                        sub_board_symbols.add(cell_value)
    
    return True
```

### **Why This Works:**
- **Set-Based Detection:** O(1) duplicate checking for each constraint
- **Simultaneous Checking:** Validates rows and columns in single pass
- **Sub-board Iteration:** Systematically covers all regions without overlap
- **Early Termination:** Returns False immediately upon finding violation

### **Example Walkthrough:**
**Input:** 4×4 board with symbols [@, #, &, *]

```
@ . . .
. * . #
# . * &
* & . @
```

---

