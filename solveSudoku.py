class Sudoku:
    board = []
    EMPTY = '.'
    DIGITS = set([str(num) for num in range(1, 10)]) # SET of STRINGS
    
    def __init__(self, _grid: list[list[str]]):
        self.board = _grid
        
    def print_board(self):        
        for row in range(9):
            # print(self.board[row])
            for col in range(9):
                if (col % 3 == 1):
                    print(" ", self.board[row][col], " ", end='')
                    # print(" ", col, " ", end='')
                    if ((col + 1) % 3 == 0):
                            print("|", end='')
                else:
                    if (col == 9 - 1):
                        print(self.board[row][col])
                        # print(col)
                    else:
                        
                        print(self.board[row][col], end='')
                        # print(col, end='')
                        if ((col + 1) % 3 == 0):
                            print(" | ", end='')

                
                    
            if (row != 0 and row % 3 == 2 and row != 9 - 1):
                print("---" * 9)
    
    # def solve(self, board: list[list[str]] ) -> None:
    def solve(self) -> None:
        self.is_valid_state(self.board)
        
    def is_valid_state(self, board):
        for row in range(9): # Check if all rows are all 1-9            
            if not set(self.board[row]) == self.DIGITS: # DIGITS is a set
                return False
            
        for col in self.get_cols():
            if not set(col) == self.DIGITS:
                return False
            
        for grid in self.get_sub_grids():
            if not set(grid) == self.DIGITS:
                return False
        
        return True
    
    def get_cols(self):
        all_cols = []
        
        for i in range(9):
            all_cols.append(list())
            for j in range(9):
                all_cols[i].append(self.board[j][i])
        
        return all_cols
    
    def get_sub_grids(self):
        all_grids = []
        # for i in range(9):
        #     all_grids.append(list())

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                sub_grid = []
                for iterator in range(3):
                    sub_grid.extend(self.board[row + iterator][col:col + 3]) # add lists into sub_grid as elements instead of lists
                    
                all_grids.append(sub_grid)

        # for i in range(len(all_grids)):
        #     print(all_grids[i])

        return all_grids
    
    def get_row_used_digits(self, row):
        used_digits = set()
        used_digits.update(self.board[row])
        
        
    
    # def get_available_digit(self, board, row, col, get_grid_at_pos(row, col) ):
    #     pass
    

s_grid = list(int(n) for n in range(9))
f_grid = []
f_grid.extend([s_grid.copy() for i in range(9)])



sample_1 = [
    ['3', '8', '6', '.', '.', '4', '7', '.', '.'],
    ['.', '1', '9', '.', '.', '.', '.', '2', '.'],
    ['.', '2', '.', '1', '.', '3', '8', '.', '5'],
    ['1', '7', '8', '.', '3', '.', '6', '2', '.'],
    ['6', '5', '2', '.', '.', '1', '.', '.', '4'],
    ['9', '4', '3', '2', '7', '.', '.', '.', '.'],
    ['2', '3', '1', '7', '4', '9', '5', '8', '6'],
    ['8', '.', '.', '.', '1', '.', '4', '.', '.'],
    ['4', '.', '.', '.', '.', '.', '.', '.', '2']
]

sudoku_board = Sudoku(sample_1)
# sudoku_board = Sudoku(f_grid)
sudoku_board.print_board()
sudoku_board.solve()

# for i in sample_1:
#     print(set(i) == sudoku_board.DIGITS)