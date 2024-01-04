class Sudoku:
	board = []
	EMPTY = '.'
	DIGITS = set([str(num) for num in range(1, 10)]) # SET of STRINGS
	
	def __init__(self, _grid: list[list[str]]):
		self.board = _grid
		
	def print_board(self, board):        
		for row in range(9):
			for col in range(9):
				if (col % 3 == 1):
					print(" ", board[row][col], " ", end='')
					if ((col + 1) % 3 == 0):
							print("|", end='')
				else:
					if (col == 9 - 1):
						print(board[row][col])
					else:
						print(board[row][col], end='')
						if ((col + 1) % 3 == 0):
							print(" | ", end='')

			if (row != 0 and row % 3 == 2 and row != 9 - 1):
				print("---" * 9)
	
	def solve(self) -> None:
		# self.print_board()
		modified_board = self.board.copy()
		
		if self.is_valid_state() == False: # still unfinish
			for i in range(9):
				for j in range(9):
					if modified_board[i][j] == '.': # empty
						tempTries = self.get_available_digits(i, j)
						for tries in tempTries:
							modified_board[i][j] = tries
							if (self.solve() == True):
								return True
							else: 
								modified_board[i][j] = '.'
							
						print("Returned false on [", i, "][", j, "]=", sep="")
						return False # track back if all current tries is failed

		print("This board is done?")
		self.print_board(modified_board)
		return True
		
		
	def is_valid_state(self):
		for row in self.get_rows(): # Check if all rows are all 1-9            
			if not set(row) == self.DIGITS: # DIGITS is a set
				return False

		for col in self.get_cols():
			if not set(col) == self.DIGITS:
				return False

		for grid in self.get_sub_grids():
			if not set(grid) == self.DIGITS: 
				return False
		
		return True
	
	def get_rows(self):
		return self.board
	
	def get_cols(self):
		all_cols = []
		
		for i in range(9):
			all_cols.append(list())
			for j in range(9):
				all_cols[i].append(self.board[j][i])
			# print(all_cols[i])
			
		return all_cols
	
	def get_sub_grids(self):
		all_grids = []

		for row in range(0, 9, 3):
			for col in range(0, 9, 3):
				sub_grid = []
				for iterator in range(3):
					sub_grid.extend(self.board[row + iterator][col:col + 3]) # add lists into sub_grid as elements instead of lists
				all_grids.append(sub_grid)

		return all_grids
	
	def get_grid_position(self, row, col):
		grid = int()
		multiplier = 0
		if (row >= 3):
			multiplier = 1
		if (row >= 6):
			multiplier = 2
		return 3 * multiplier + int(col/3)
	
	def get_available_digits(self, row, col):
		used_digits = set()
		available_digits = set([str(digit) for digit in range(1, 10)])
		
		used_digits.update(self.get_rows()[row])
		used_digits.update(self.get_cols()[col])
		used_digits.update(self.get_sub_grids()[self.get_grid_position(row, col)])
		
		# print("will be picked: ", available_digits.difference(used_digits))
		
		return available_digits.difference(used_digits)

s_grid = list(int(n) for n in range(9))
f_grid = []
f_grid.extend([s_grid.copy() for i in range(9)])



sample_1 = [
	['.', '.', '.', '.', '6', '.', '1', '.', '7'],
	['.', '1', '.', '3', '.', '2', '.', '9', '.'],
	['.', '7', '.', '8', '.', '.', '.', '.', '2'],
	['1', '4', '5', '.', '.', '7', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '4'],
	['3', '.', '.', '2', '.', '.', '.', '5', '.'],
	['.', '.', '8', '1', '.', '.', '5', '.', '.'],
	['.', '5', '.', '.', '.', '8', '.', '.', '3'],
	['2', '.', '1', '.', '.', '5', '.', '.', '.']
]


sample_2 = [
    ["2", "6", ".", ".", "7", ".", "4", "8", "3"],
    ["3", "1", ".", ".", ".", ".", ".", ".", "9"],
    ["5", "7", ".", "3", "4", ".", ".", ".", "2"],
    ["1", ".", ".", ".", ".", ".", "9", ".", "."],
    [".", "8", ".", ".", "9", ".", ".", "3", "."],
    [".", ".", "7", ".", ".", ".", ".", ".", "5"],
    ["7", ".", ".", ".", "5", "2", ".", "9", "4"],
    ["8", ".", ".", ".", ".", ".", ".", "5", "7"],
    ["9", "5", "6", ".", "3", ".", ".", "2", "1"]
]
# sudoku_board = Sudoku(sample_1)
sudoku_board = Sudoku(sample_2)
# sudoku_board = Sudoku(f_grid)
# print("Initial board")
# sudoku_board.print_board(sudoku_board.board)
sudoku_board.solve()