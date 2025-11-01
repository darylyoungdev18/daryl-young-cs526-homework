"""
You are given an array A[1…n] which contains the cumulative snowfall totals for n consecutive days. For example, if there are 6 inches on snow on day 1, 7
inches of snow on day 2, 0 inches of snow on day 4 and 4 inches of snow on day 4 the array would contain the values [6,13,13,17].
You should read an input file from standard in which will contain 2 lines, the first line will be the number of days and the second line will be the a comma
separated set of cumulative snowfall totals
Design and implement an algorithm that determines if there exists three consecutive days that produced more than half of the total snowfall across the n days.
Your solution should return either YES or NO.


You should demonstrate your code as run with the sample input on the following slide. You may run all of the inputs in a
single execution of your code or individually. Your output should be structured as the input you are testing followed by your
solution.
"""

#being that the array is constanly increasing we need to find the third dat and compare it to the total divided by 2
# i should see if there is even three days first
#then I can pull the third day and compare it to len(array) / 2 i think
#I should also have a case if there are three days return yes right away
def has_three_day_snowfall_exceeding_half(cumulative_snowfall):
    n = len(cumulative_snowfall)
    
    if n < 3:
        return "NO"
    
    total_snowfall = cumulative_snowfall[-1]
    half_total = total_snowfall / 2
    
    for i in range(2, n):
        three_day_snowfall = cumulative_snowfall[i] - cumulative_snowfall[i - 3]
        if three_day_snowfall > half_total:
            return "YES"
    
    return "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    num_days = int(data[0])
    cumulative_snowfall = list(map(int, data[1].split()))
    
    result = has_three_day_snowfall_exceeding_half(cumulative_snowfall)
    print(f"Input: {cumulative_snowfall} -> {result}")


if __name__ == "__main__":
    main()