valid_sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
       


## Check if the number is in the 3x3 grid

def new_checker(input_board):
    
    ## Check if row is good
    for row in input_board: 
        if not is_valid_set(row):
            return False
        
    ## Check if column is good
    for col in zip(*input_board):
        if not is_valid_set(col):
            return False
    
    ## Check if 3x3 grid is good
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [input_board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_set(square):
                return False
    return True
        
def is_valid_set(row_of_nums):
    seen = set()
    
    for num in row_of_nums: 
        if num != 0: 
            if num in seen: 
                return False
            seen.add(num)

    return True

print(new_checker(valid_sudoku_board))
