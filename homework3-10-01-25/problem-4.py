def lines_intersect(line1, line2):
    """
    Check if two infinite lines intersect (streams go both directions)
    Uses algebraic method - no CCW needed
    """
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    
    # Direction vectors
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    
    # Cross product of direction vectors
    cross = dx1 * dy2 - dy1 * dx2
    
    # If cross product is 0, lines are parallel (don't intersect)
    if abs(cross) < 1e-10:
        return False
    
    # Non-parallel infinite lines always intersect
    return True

def parse_input():
    """Parse input - handles both spaced and compact formats"""
    try:
        n = int(input().strip())
        ghostbusters = []
        ghosts = []
        
        for _ in range(n):
            line = input().strip()
            
            if ' ' in line:
                # Spaced format: "B 0 0 G 1 1"
                tokens = line.split()
                i = 0
                while i < len(tokens):
                    if tokens[i] == 'B':
                        x, y = int(tokens[i+1]), int(tokens[i+2])
                        ghostbusters.append((x, y))
                        i += 3
                    elif tokens[i] == 'G':
                        x, y = int(tokens[i+1]), int(tokens[i+2])
                        ghosts.append((x, y))
                        i += 3
                    else:
                        i += 1
            else:
                # Compact format: "B00G11"
                i = 0
                while i < len(line):
                    if line[i] == 'B':
                        x, y = int(line[i+1]), int(line[i+2])
                        ghostbusters.append((x, y))
                        i += 3
                    elif line[i] == 'G':
                        x, y = int(line[i+1]), int(line[i+2])
                        ghosts.append((x, y))
                        i += 3
                    else:
                        i += 1
        
        return ghostbusters, ghosts
    except:
        return [], []

def solve_recursive(ghostbusters, ghosts):
    """
    Dummy recursive solution placeholder.
    Replace this with your actual recursive logic.
    """
    # For now, just return True if the number of ghostbusters is at least the number of ghosts
    return len(ghostbusters) >= len(ghosts)

def can_eliminate_all_ghosts(ghostbusters, ghosts):
    """Wrapper function for your recursive solution"""
    if len(ghostbusters) == 0:
        return True
    return solve_recursive(ghostbusters, ghosts)


def main():
    # Parse input
    ghostbusters, ghosts = parse_input()
    
    # Debug output (optional)
    print(f"Ghostbusters: {ghostbusters}")
    print(f"Ghosts: {ghosts}")
    
    # Check if all ghosts can be eliminated
    if can_eliminate_all_ghosts(ghostbusters, ghosts):
        print("All Ghosts: were eliminated")
    else:
        print("All Ghosts: were not eliminated")

if __name__ == "__main__":
    main()