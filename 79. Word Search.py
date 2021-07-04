# https://www.youtube.com/watch?v=ve2ZMiB1INI&ab_channel=SaiAnishMalla
class Solution():
    def exist(self, board, word):
            row=len(board)
            col=len(board[0])
            def check(r,c, index):
                if r>=row or r<0 or c>=col or c<0:
                    return False
                if board[r][c]!=word[index]:
                    return False
                if index+1==len(word):
                    return True
                index+=1
                temp=board[r][c]
                board[r][c]="@"
                b=check(r+1,c, index) or check(r-1,c, index) or check(r,c+1, index) or check(r,c-1, index)
                board[r][c]=temp
                return b


            for r in range(row):
                for c in range(col):
                    if board[r][c]==word[0]:
                        bol=check(r,c,0)
                        if bol==True:
                             return True
            return False

a=Solution()
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word= "ABCCED"
print(a.exist(board,word))
