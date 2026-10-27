class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) #keep tracks of numbers seen in columns
        rows = defaultdict(set) #keep tracks of numbers seen in rows
        squares = defaultdict(set)#tracks numbers seen in each 3x3 sub-box
                                #(r // 3, c // 3) gives you the index of the 3x3 square the cell belongs to (0, 1, or 2 for each)

        for r in range(9): #loops through each cell in the 9x9 board
            for c in range(9): #loops through each cell in the 9x9 board
                if board[r][c] == ".": #skips empty cells
                    continue
                    #If the value at board[r][c] is already present in:
                if ( board[r][c] in rows[r] #the current rows
                    or board[r][c] in cols[c] #the current column
                    or board[r][c] in squares[(r // 3, c // 3)]):#checks whether the current number already exists in the 3x3 sub-grid (box) that the cell (r, c) belongs to.
                    return False #Then the board is invalid → return False.

                #If no violation is found, add the value to the respective row, column, and square sets.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

#squares[(r // 3, c // 3)]
#r // 3 and c // 3 divide the row and column by 3 using integer division.
#This gives you the index of the 3x3 square the cell belongs to.