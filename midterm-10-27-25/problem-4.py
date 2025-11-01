#I am given a puzzle board with n x n with the square root being an integer
#The board is populated with symbols where the number of symbols is equal to n.
#Example: A partially filled 4x4 puzzle board with symbols: [@#&*] with a . representing a non-filled position
"""
@ . . .
. * . #
# . * &
* & . @
"""
#Create and code an algorithm to calculate if the current board is in a valid or invalid state. The board is
#considered valid if the following conditions are met:
#• Each row must contain each symbol at most once
#• Each column must contain each symbol at most once
#• The board contains sub-boards of size square root of n and each sub-board must contain each symbol at most
#once


#this is similar to the problem with look at in class earlier where there was a total to the table but we also focus on the sub table
#aka the table within the table
#so in the 4x4 example there are 4 sub tables of 2x2
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

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])
    symbols = data[1].split(',')
    
    # Fix the board parsing to handle different formats
    board = []
    for i in range(n):
        row_data = data[i + 2]
        
        # If row has spaces, split by spaces
        if ' ' in row_data:
            row = row_data.split()
        else:
            # If no spaces, split each character
            row = list(row_data)
        
        board.append(row)
    
    result = is_valid_puzzle_board(board, symbols)
    validity = "VALID" if result else "INVALID"
    print(f"Input Board:\n" + "\n".join([" ".join(row) for row in board]) + f"\n-> {validity}")

if __name__ == "__main__":
    main()