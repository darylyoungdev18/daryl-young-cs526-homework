# CS526 Homework 4
**Due Date:** October 22, 2025

---

## Problem 2: Smallest Number of Elements (Greedy Algorithm)

### **The Heart of the Algorithm:**
**Greedy Selection with Sorted Descending Order**
- Sort numbers from largest to smallest
- Greedily select elements starting with the largest
- Count how many elements needed to reach or exceed target sum

### **Key Questions Asked:**
1. **How do I get the largest numbers seen first?**

2. **Why does selecting largest first work?**
  
3. **When do we stop?**
  
### **Algorithm Core:**
```python
def smallest_number_elements(num, target):
    # Sort from greatest to smallest
    num.sort(reverse=True)
    
    total = 0 
    count = 0
    
    # Greedily add largest elements
    for n in num:
        total += n
        count += 1
        
        # Stop when target reached
        if total >= target:
            return count
    
    # Target cannot be reached
    return -1
```

### **Why This Works:**
- **Greedy Property:** Selecting largest elements first minimizes count
- **Optimal Substructure:** If largest k elements reach target, no smaller k exists



---

## Problem 3: Count Right Triangles (Computational Geometry)

### **The Heart of the Algorithm:**
**Slope-Based Perpendicularity Detection**
- For each point, calculate slopes to all other points
- Find pairs of slopes that are perpendicular (product = -1)
- Use mathematical property: perpendicular slopes multiply to -1
- Avoid double-counting triangles using proper indexing

### **Key Questions Asked:**

1. **How do I find slopes relative to one point?**
  
2. **How do I count the pairs of slopes that are perpendicular?**
 
3. **How do I avoid counting the same triangles?**
   
### **Algorithm Core:**
```python
def count_right_triangles(points):
    n = len(points)
    count = 0
    
    # For each potential right-angle vertex
    for i in range(n):
        slopes = {}  # Map: slope -> list of point indices
        
        # Calculate slopes from point i to all other points
        for j in range(n):
            if i == j:
                continue
            
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            
            # Calculate slope (handle vertical lines)
            if dx == 0:
                slope = float('inf')  # Vertical line
            else:
                slope = dy / dx
            
            # Store this slope and point index
            if slope not in slopes:
                slopes[slope] = []
            slopes[slope].append(j)
        
        # Find perpendicular pairs
        for slope1 in slopes:
            # Find perpendicular slope: m₁ × m₂ = -1, so m₂ = -1/m₁
            if slope1 == 0:
                slope2 = float('inf')  # Perpendicular to horizontal is vertical
            elif slope1 == float('inf'):
                slope2 = 0  # Perpendicular to vertical is horizontal
            else:
                slope2 = -1 / slope1
            
            # If perpendicular slope exists, count triangles
            if slope2 in slopes:
                # Number of triangles = points on slope1 × points on slope2
                count += len(slopes[slope1]) * len(slopes[slope2])
        
        # Divide by 2 because each pair counted twice (slope1, slope2) and (slope2, slope1)
        count //= 2
    
    return count
```

### **Why This Works:**
- **Geometric Property:** Right triangles have perpendicular sides (m₁ × m₂ = -1)
- **Vertex-Centric:** By fixing the right angle vertex, we avoid duplicates
- **Complete Coverage:** Checking all points as potential vertices ensures no triangles missed
- **Efficient Counting:** Use multiplication principle for pairs from two perpendicular slope groups

### **Mathematical Foundation:**
```
For perpendicular lines:
- If slope₁ = m, then slope₂ = -1/m
- Special cases:
  * Horizontal (slope = 0) ⊥ Vertical (slope = ∞)
  * slope = 1 ⊥ slope = -1
  * slope = 2 ⊥ slope = -1/2
```
