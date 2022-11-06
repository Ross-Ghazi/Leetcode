class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # if there is an answer it is either tops[0],bottoms[0]
        options=[tops[0],bottoms[0]]
        candidates=[]
        for n in options:
            for i in range (len(tops)):
                if tops[i]!=n and bottoms[i]!=n:
                    break
            else:
                candidates.append(n)
        # if thre is no number that appear on all indexes of either top or bottom
        # there is no solutio    
        if len(candidates)==0:
            return -1
    
        res=float("inf") 
        for n in candidates:
            #you cannot find rotation2 base on rotation1, 
            #it should be calculated separately
            rotation1,rotation2=0,0 
            for i in range(len(tops)):
                if tops[i]!=n:
                    rotation1+=1
                if bottoms[i]!=n:
                    rotation2+=1           
            res=min(res,rotation2,rotation1)
        return res
        
