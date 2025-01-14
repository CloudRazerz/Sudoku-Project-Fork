import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
create a sudoku board - initialize class variables and set up the 2D board
This should initialize:
self.row_length - the length of each row
self.removed_cells - the total number of cells to be removed
self.board - a 2D list of ints to represent the board
self.box_length - the square root of row_length

Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

Return:
None
    '''

    def __init__(self, row_length, removed_cells):

        ##initialize variables
        self.row_length = 9#row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length))
        no_dup_col_count = 0
        rand_num_row = []
        rand_num_col = []
        self.removed_cells_copy = removed_cells
        self.board= [[0 for _ in range(self.row_length)] for _ in range(self.row_length)]


    '''
Returns a 2D python list of numbers which represents the board

Parameters: None
Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

Parameters: None
Return: None
    '''

    def print_board(self):
        print(self.board)

    '''
Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

Parameters:
row is the index of the row we are checking
num is the value we are looking for in the row

Return: boolean
    '''

    def valid_in_row(self, row, num):
        i = 0
        #print("numum" + str(num) + " row " + str(row))
        for i in range(len(self.board)):
            if self.board[row][i] == num:
                #print("yes row " + str(self.board[row][i]))
                return False
            #else:
             #   return False
        #print("no row")
        return True

    '''
Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

Parameters:
col is the index of the column we are checking
num is the value we are looking for in the column

Return: boolean
    '''

    def valid_in_col(self, col, num):
        i = 0
        for i in range(len(self.board)):
            if self.board[i][col] == num:
                #print("yes col")
                return False
            #else:
             #   return True
        #print("no col")
        return True

    '''
Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

Parameters:
row_start and col_start are the starting indices of the box to check
i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
num is the value we are looking for in the box

Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        i = 0
        j = 0
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[int(row_start + i)][int(col_start + j)] == num:
                    return False
                #else:
                 #   return True
        return True
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

Parameters:
row and col are the row index and col index of the cell to check in the board
num is the value to test if it is safe to enter in this cell

Return: boolean
    '''

    def is_valid(self, row, col, num):
        if self.valid_in_box(row-row % self.box_length,col - col % self.box_length,num) and self.valid_in_col(col,num) and self.valid_in_row(row,num) :
            return True
        else:
            return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

Parameters:
row_start and col_start are the starting indices of the box to check
i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

Return: None
    '''

    def fill_box(self, row_start, col_start):
        num=0
        for i in range(self.box_length):
            for j in range(self.box_length):
                while True:
                    num=self.randomGen(self.row_length)
                    if self.valid_in_box(row_start,col_start,num):
                        break
                self.board[row_start+i][col_start+j] = num
    def randomGen(self,num):
        return math.floor(random.random()*num +1)
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

Parameters: None
Return: None
    '''

    def fill_diagonal(self):
        for i in range(0,self.row_length,self.box_length):
            self.fill_box(i,i)
    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

Parameters:
row, col specify the coordinates of the first empty (0) cell

Return:
boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def generate_sudoku(self, size, removed):

        # comment print board out when finished changing sudoku_generator.py
        #self.print_board()

        self.fill_values()
        board = self.get_board()
        self.remove_cells()
        board = self.get_board()
        return board

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

Parameters: None
Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        if (self.fill_remaining(0, self.box_length)):
            self.board_copy = self.board

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

Parameters: None
Return: None
    '''

    def remove_cells(self):
        ##remove cells
        # print(self.removed_cells)
        for i in range(self.removed_cells_copy - sum(x.count(0) for x in self.board)):
            rand_num1 = random.randrange(0, self.row_length)
            rand_num2 = random.randrange(0, self.row_length)

            # only remove cell if it has not already been removed
            while self.board[rand_num1][rand_num2] == 0:
                rand_num1 = random.randrange(0, self.row_length)
                rand_num2 = random.randrange(0, self.row_length)
                if self.board[rand_num1][rand_num2] != 0:
                    self.board[rand_num1][rand_num2] = 0
                    break
            else:
                self.board[rand_num1][rand_num2] = 0
                # print("Popped location:", rand_num1, rand_num2)

            self.board_for_user = self.board
#fill
    def fill_in_sudoku(self):
        # loops = 0
        i = 0
        j = 0
        # k = 1
        backtrack = False
        board_for_solver_copy = self.board.copy()
        num_zeros = sum(x.count(0) for x in self.board)
        # loops += 1
        # if loops == 10:
        # self.board == board_for_solver_copy
        # i += 1
        # j += 1
        # loops = 0
        while True:
            while i < self.row_length:
                # print("while loop 1")
                j = 0
                while j < self.row_length:
                    num_zeros = sum(x.count(0) for x in self.board)
                    #print("numzero" + str(num_zeros))
                    if num_zeros == 0:
                        return self.board
                    #print(self.board)
                    # print("while loop 2")
                    #print(i, j)
                    if self.board[i][j] == 0:
                        if backtrack:
                            #print("worked again")
                            # self.board[i][j] += 1
                            backtrack = False
                            # continue
                        #print(f"zero found at {i},{j}")
                        k = 1
                        for k in range(1,10):
                            #print("for loop k " + str(k))
                            if self.valid_in_col(j, k):
                                if self.valid_in_row(i, k):
                                    #print("valid col")
                                    #if self.valid_in_row(i, k):
                                    #print("valid row")
                                    #print("is_valid")

                                    #print("self.board")
                                    self.board[i][j] = k
                                   # break
                                # test
                               # if self.board[i][j] != board_for_solver_copy:
                                #    print("works")
                                    #print( "new board " + str(self.board))
                                    break
                            #if k == self.row_length - 1:
                             #   backtrack = True

                    if not backtrack:
                        j += 1
                    else:
                        j -= 1

                    if j == -1:
                        i -= 1
                        if i == -1:
                            i = self.row_length - 1
                        j = self.row_length - 1
                if backtrack == False:
                    i += 1
                else:
                    i -= 1

                #print("check")
                if i == -1:
                    i = self.row_length - 1
                elif i == 9:
                    i = 0

            # print("Zeros found:", zeros_found)

        #print(self.board)


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    #sudoku.fill_in_sudoku()

    #comment print board out when finished changing sudoku_generator.py
    #sudoku.print_board()

    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board