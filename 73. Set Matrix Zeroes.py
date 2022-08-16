# constant space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])        
        def dfs(r,c):
            for c1 in range(col):
                if  matrix[r][c1]!=0: matrix[r][c1]="*" 
            for r1 in range(row):
                if  matrix[r1][c]!=0: matrix[r1][c]="*"             
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    dfs(r,c)
        for r in range(row):
            for c in range(col):
                if matrix[r][c]=="*":
                     matrix[r][c]=0
        return matrix
######################################################
# O(m + n) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:     
        row=len(matrix)
        col=len(matrix[0])              
        rowSet=set()
        colSet=set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    rowSet.add(r)
                    colSet.add(c)
        for r in range(row):
            for c in range(col):
                if r in rowSet or c in colSet:
                    matrix[r][c]=0
        return matrix
######################################################
        
