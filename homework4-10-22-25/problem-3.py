import sys
import time


# this is counting the total unique right triangles that can be created from a list of 2D points

def count_right_triangles(points):
    total_right_triangles = 0
    number_of_points = len(points)

    start_time = time.perf_counter()
    for index_fixed_point in range(number_of_points):
        #created an empty dictionary to hold my slopes
        # each key = slope value, each value = how mnay lines have the same slope
        slope_count = {}
        x_fixed, y_fixed = points[index_fixed_point]

        #picked a fixed point then fined slopt to all other points
        for index_other_point in range(number_of_points):
            if index_fixed_point == index_other_point:
                continue

            x_other, y_other = points[index_other_point]
            delta_x = x_other - x_fixed
            delta_y = y_other - y_fixed

            # this is special cases  such as undefines
            if delta_x == 0:
                slope = 'vertical'
            elif delta_y == 0:
                slope = 'horizontal'
            else:
                slope = delta_y / delta_x 



            if slope not in slope_count:
                slope_count[slope] = 0
            slope_count[slope] += 1


        # next count perpendicular slope pairs for this vertex(point)
        for slope, count in slope_count.items():
            if slope== "vertical":
                perpendicular_slope = "horizontal"
            elif slope == "horizontal":
                perpendicular_slope = "vertical"
            else:
                perpendicular_slope = -1 / slope

            if perpendicular_slope in slope_count:
                total_right_triangles += count * slope_count[perpendicular_slope]

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print(f"Execution Time: {execution_time:.6f} seconds")


    #each triangle is counted only once because the right angle occurs
    # at a specific vertex(point) not at other corners.
    return total_right_triangles

if __name__ == "__main__":
    # Input format example (in a file like right_triangles_input.txt):
    # 5
    # 0 0
    # 0 4
    # 3 0
    # 7 3
    # 9 0

    input_data = sys.stdin.read().strip().split()
    number_of_points = int(input_data[0])

    points = []
    index = 1
    for _ in range(number_of_points):
        x_coordinate = int(input_data[index])
        y_coordinate = int(input_data[index + 1])
        points.append((x_coordinate, y_coordinate))
        index += 2

    # Compute and print result
    result = count_right_triangles(points)
    print(f"The number of right triangles is: {result}")

