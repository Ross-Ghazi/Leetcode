class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])        
        r=0
        c=col-1        
        while True:
            if r>=row or c<0:
                return False
            if target==matrix[r][c]:
                return True
            if target>matrix[r][c]:
                r+=1
            else:
                c-=1
        return False
###############################################    
#second method 
# using binary search
# change 2D array to 1D
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col=len(matrix[0])#4
        row=len(matrix) #3
        start=0
        end=(col*row)-1
        
        while True:
            if start>end:
                return False 
            mid=(start+end)//2
            c=mid%col
            r=mid//col
            if matrix[r][c]==target:
                return True
            
            elif matrix[r][c]<target:
                start=mid+1
            else:
                end=mid-1
            print(r,c,mid)
        return False 
    
# link: https://github.com/Rouzbeh1797/Leetcode/blob/main/Binary%20Search.py
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if target<matrix[0][0] or target>matrix[-1][-1]:
#             return False
#         def BsearchRow(l,r):
#             if l>r:
#                 return r
#             mid=(l+r)//2
#             if matrix[mid][0]==target:
#                 return mid
#             if matrix[mid][0]>target:
#                 r=mid-1
#                 return BsearchRow(l,r)
#             else:
#                 l=mid+1
#                 return BsearchRow(l,r)
#         row=BsearchRow(0,len(matrix)-1)
#         def BsearchCol(l,r):
#             if l>r:
#                 return False
#             mid=(l+r)//2
#             if matrix[row][mid]==target:
#                 return True
#             if matrix[row][mid]>target:
#                 r=mid-1
#                 return BsearchCol(l,r)
#             else:
#                 l=mid+1
#                 return BsearchCol(l,r)
        
#         return BsearchCol(0,len(matrix[0])-1)
            
