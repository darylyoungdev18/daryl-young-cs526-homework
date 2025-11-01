"""
You are going shopping at your local store. The aisles are organized such that each aisle contains a specific category of item. The aisles are
arranged from left to right. The aisles are represented by an array of categories e.g.
[‘dinner’, ‘lunch’, ‘breakfast’, ‘snacks’, ‘desserts’]
You want to collect as many items as you can moving through the aisles from left to right. The store owner has some very strict rules for the
shoppers:
• You have only 2 baskets to place your items in and each basket can hold only a single category of item.
• Starting from the aisle of your choice, you must select exactly one item from the aisle and place it in one of your baskets, remember
that you have only 2 baskets and each basket can contain only one category of item.
• Once you reach an aisle that contains an item you are not allowed to put into either of your baskets you must stop shopping.
"""


"""
Shopping Cart
You will be given input files with the first line containing the number of aisles and line two containing a comma separated list of categories
e.g. file 1:
3
dinner,lunch,dinner
e.g. file 2:
5
dinner,lunch,breakfast,lunch,lunch
Write an algorithm which will return the maximum number of items you can select from the given aisle category input as
“<items> items were selected”.
e.g. Input: [‘dinner’, ‘lunch’, ‘dinner’] -> 3 items were selected
e.g. Input: [‘dinner’, ‘lunch’, ‘breakfast’, ‘lunch’, ‘lunch’] -> 4 items were selected

"""


#understand the rule at most you can pick up two of the same items after that it stops if there is a third
def max_items_selected(aisles):
    if not aisles:
        return 0

    basket = set()
    count = 0

    for category in aisles:
        if category in basket or len(basket) < 2:
            basket.add(category)
            count += 1
        else:
            break

    return count

#use inputs from text file or standard input to test the function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    n = int(data[0])
    aisles = data[1].split(',')

    result = max_items_selected(aisles)
    print(f"{result} items were selected")

    #heart of the algorithm is to use a set to track the categories in the baskets and a counter to count the items selected.
    # I iterate through the aisles and check if the category can be added to the baskets or not based on the rules provided.

    # questions I asked myself:
    # 1. What if the input list is empty? -> return 0
    # 2. What if all aisles have the same category? -> return length of aisles
    # how am I going to show  items going into the baskets? -> using a set to track unique categories