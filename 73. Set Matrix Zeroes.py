
# no refernce
# the idea is loop through the matrix if you see zero make all of  items in same col or raw to "" (other than other zeros)
# thenm change all "" to zeros. similat to leetoce 289
# for zero function: I had initally looping through the whole matrix but there is no need to do that
# we can loop through only the col and row that we are intersted
# Also fir zero function first I was not had "if matrix[r0][c] !=0" which cause some bugs as it will change zeros to "" and then you will not change its col or rows as it is not 0 anymore

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        def zero(r0,c0):  
            # I had initally looping through the whole matrix but there is no need to do that
            # we can loop through only the col and row that we are intersted
            # for ro in range(row):
            #     for co in range(col):
            #         if ro==r and matrix[ro][co] !=0 :
            #              matrix[ro][co]=""
            #         if co==c and matrix[ro][co] !=0:
            #             matrix[ro][co] =""
            for c in range (col):
                if matrix[r0][c] !=0 :
                    matrix[r0][c]="" 
            for r in range (row):
                if matrix[r][c0] !=0 :
                    matrix[r][c0]="" 
                        
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    zero(r,c)
        print(matrix)
        for r in range(row):
            for  c in range(col):
                if matrix[r][c]=="":
                    matrix[r][c]=0
        
