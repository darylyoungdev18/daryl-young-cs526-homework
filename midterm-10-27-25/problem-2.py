"""
You are in a square state with 25 counties. The counties can be arranged into an NxN grid (for our inputs 5x5). Two counties are neighbors if they are horizontally or vertically next to each other.
Some of the counties contain people infected by a mysterious virus which is highly contagious. If a county has an infected person, that person never becomes healthy and the county is considered infected. Each day the infection spreads to healthy counties if that county has at least two infected neighbors.
Write an algorithm to calculate if the infection will stop spreading and there are any healthy counties left in the state. 
You will be given 2 input files which have the form:
Size of matrix
List of coordinate cells of initially infected counties
e.g.
5
1 3
2 2
3 4
This input means that the input matrix is 5x5 and cells (1,3), (2,2), (3,4) are initially infected

"""
def are_there_healthy_counties_after_infection(n, infected_coords):
    #initialize the grid with healthy counties based on input size n
    grid = [[0 for i in range(n)] for j in range(n)]
    #mark the infected counties in the grid
    for infected_counties in infected_coords:
        x, y = infected_counties
        grid[x][y] = 1 # 1 represents infected county
    #function to count infected neighbors of a county
    def count_infected_neighbors(x, y):
        infected_count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        for direction_x, direction_y in directions:
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if 0 <= neighbor_x < n and 0 <= neighbor_y < n:
                if grid[neighbor_x][neighbor_y] == 1:
                    infected_count += 1
        return infected_count
    #simulate the infection spread day by day
    infection_spread = True
    while infection_spread:
        infection_spread = False
        new_infections = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: # healthy county
                    infected_neighbors = count_infected_neighbors(i, j)
                    if infected_neighbors >= 2:
                        new_infections.append((i, j))
        for x, y in new_infections:
            grid[x][y] = 1 # mark as infected
            infection_spread = True
    #check if there are any healthy counties left
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return True # healthy county found
    return False # no healthy counties found



# use inputs from text file or standard input to test the function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])  # size of the grid
    infected_coords = []
    for line in data[1:]:
        x, y = map(int, line.split())
        infected_coords.append((x, y))
    
    result = are_there_healthy_counties_after_infection(n, infected_coords)
    if result:
        print("There are healthy counties left after infection spread.")
    else:
        print("All counties are infected after infection spread.")


#heart of the code is an simulation problem that requires me to 
#iterate through the grid and check each county's neighbors
# then I need to see if there are two infected neighbors
# if there are two infected neighbors I need to mark that county as infected
# key questions I asked is how to record the grid
# how would I represent infected vs healthy
#how to iterate through the days to 