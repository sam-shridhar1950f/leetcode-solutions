class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (
                r not in range(rows)
                or c not in range(cols)
                or board[r][c] is not word[i]
            ):
                return False
            
            temp = board[r][c]
            board[r][c] = '#' 
            
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            
            board[r][c] = temp  
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
