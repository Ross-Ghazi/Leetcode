#https://leetcode.com/problems/word-search/discuss/747144/Python-dfs-backtracking-solution-explained/1531990
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        flag=False        
        if len(word) > row*col:
            return False
        
        # without optimization it will gives time exceed error
        # perform two optimizations to avoid time exceed error
        
        #optimization 1
        #count of a LETTER in word is Greater than count of it being in board
        count = Counter(sum(board, []))                
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
        
        #optimization 2        
        # if count of 1st letter of Word(A) is Greater than that of Last One in Board(B). 
        # Reverse Search the word then search as less case will be searched.
        # lets say the word is "ABCCED":
        # if count("A") in board is more than count("D") then reverse word, so search less 
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
                
                
                
        def check(r,c,index):
            nonlocal flag
            if index>=len(word):
                flag=True
                return           
            if r<0 or c<0 or r>=row or c>=col or board[r][c]!=word[index]:
                return     
            temp=board[r][c]
            board[r][c]="*"
            dir=[(0,1),(0,-1),(-1,0),(1,0)]            
            for rr,cc in dir:
                check(r+rr,c+cc,index+1)
            board[r][c]=temp
        for r in range(row):
            for c in range(col):
                if board[r][c]==word[0]:
                    check(r,c,0)
                    if flag==True:
                        return True
        return False
                
