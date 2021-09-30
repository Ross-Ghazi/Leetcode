class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        # first from 1 to 6 we will check which nunmbers appear wither on top or bottom of all sets
        # in this example it is 2
        candidates=[]           
        for i in range(1,7):
            flag=0
            for j in range(len(tops)):
                if tops[j]!=i and bottoms[j]!=i:
                    flag=1
                    break          
            if flag==0:
                print(i)
                candidates.append(i)
        
        # if thre is no number that appear on all indexes of either top or bottom
        # there is no solution
        if len(candidates)==0:
            return -1
        
        
        # from all canidaites that we found ,we will see wihci one requires less rotation
        # number of rotation for top is number of times that it does not appear on top
        # number of rotation for bottom is number of times that it does not appear on bottom
        # we find mimimum number of rotations for all candiates        
        res=float("inf")
        for n in candidates:
            rotation1,rotation2=0,0
            for j in range(len(tops)):
                if tops[j]!=n:
                    rotation1+=1
                if bottoms[j]!=n:
                    rotation2+=1    
            res=min(res,rotation1,rotation2)
        return res
                
