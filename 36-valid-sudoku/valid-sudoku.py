class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i] or 
                    board[i][j] in col[j] or 
                    board[i][j] in square[(i // 3,j // 3)]):
                    return False
                rows[i].add(board[i][j])
                col[j].add(board[i][j])
                square[(i // 3,j // 3)].add(board[i][j])
        return True

