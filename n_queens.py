class NQueens:

    def __init__(self, N):
        self.N = N
        self.board = [['_' for _ in range(N)] for _ in range(N)]

    def n_queens(self, row):
        if row == self.N:
            return True
        
        nextRow = row + 1
        
        for i in range(self.N):
            if self.is_valid(row,i):
                self.board[row][i] = 'Q'
                if  self.n_queens(nextRow):
                    return True
                self.board[row][i] = '_'
        return False


    def is_valid(self, row, col):

        for i in range(row):
            if self.board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if self.board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Check upper-right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < self.N:
            if self.board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
                
        return True
    
    def print_board(self):
        for row in self.board:
            print(" ".join(row))

if __name__ == "__main__":
    N = 8 
    solver = NQueens(N)
    
    if solver.n_queens(0):
        print(f"\n✅ Solution found for {N}-Queens:")
        solver.print_board()
    else:
        print(f"\n❌ No solution exists for {N}-Queens.")