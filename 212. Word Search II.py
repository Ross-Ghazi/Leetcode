# https://www.youtube.com/watch?v=asbcE9mZz_U&ab_channel=NeetCode
class TrieNode:
    def  __init__(self):
        self.children={}
        self.isWord=False
    def add(self ,w):
        cur=self
        for c in w:
            if c not in cur.children:
                    cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.isWord=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()        
        for word in words: 
            root.add(word)
        
        row=len(board)
        col=len(board[0])
        res=set()
        visited=set()
        
        def dfs(r,c,wordSoFar,node):
            if r>=row or r<0 or c>=col or c<0 :
                return
            if (r,c) in visited:
                return
            if board[r][c] not in node.children:
                return
            node=node.children[board[r][c]]
            visited.add((r,c))
            wordSoFar+=board[r][c]         
            
            if node.isWord==True:
                res.add(wordSoFar)
            
            
            dfs(r+1,c,wordSoFar,node)
            dfs(r,c+1,wordSoFar,node)
            dfs(r-1,c,wordSoFar,node)
            dfs(r,c-1,wordSoFar,node)
            visited.remove((r,c))
            
        for r in range(row):
            for c in range(col):
                dfs(r,c,"", root)
        return res
    
        
        
        
