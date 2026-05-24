class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        box = [[False] * 9 for _ in range(9)]
        
        for ri,r in enumerate(board):
            for ci,c in enumerate(r):
                if c==".":
                    continue
                noi = int(c) - 1
                bi = (ri // 3) * 3 + (ci // 3)
                if row[ri][noi] or col[ci][noi] or box[bi][noi]:
                    return False
                else:
                    row[ri][noi] = True
                    col[ci][noi] = True 
                    box[bi][noi] = True
            
        
        return True