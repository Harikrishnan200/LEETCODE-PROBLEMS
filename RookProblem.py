# 999. Available Captures for Rook

# You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

# A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

# Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

# Return the number of pawns the white rook is attacking.

# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],
#                 [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
#                 [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

# Output: 3

# Explanation:

# In this example, the rook is attacking all the pawns.


# Solution

class Solution(object):
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    x_rook,y_rook = i,j
                    break
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)] # up,down,left,right
        count = 0

        for dx,dy in directions:
            x,y = x_rook,y_rook

            while 0<=x<8 and 0<=y<8:
                x += dx
                y += dy

                if not (0<=x<8 and 0<=y<8):
                    break
                elif board[x][y] == "B":
                    break

                elif board[x][y] == "p":
                    count += 1
                    break
        
        return count
    

    # ALGORITHM

    # 1. Find the position of the rook.
    # 2. Set the 4 directions and set count = 0
    # 3. For each direction, keep moving in that direction until you hit a wall or a bishop.
    # 4. If you hit a pawn, increment the count.
    # 5. Return the count.