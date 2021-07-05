# https://www.youtube.com/watch?v=Pl7mMcBm2b8&ab_channel=NickWhite
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for row in range(9):
            for col in range(9):
                if board[row][col]!=".":
                    a=str(board[row][col])+"row"+str(row)
                    b=str(board[row][col])+"col"+str(col)
                    c=str(board[row][col])+"subsq row"+str(row//3)+"col"+str(col//3)
                    if(a in seen) or (b in seen) or (c in seen):
                        return False
                    else:
                        seen.add(a)
                        seen.add(b)
                        seen.add(c)
        return True
