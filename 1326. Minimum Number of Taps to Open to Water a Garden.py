class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        #get index of x for newRange
        # searhes for any array that it starts before x
        # and return the index for the one with max end
        # if it starts after x it will break the loop
        # and return -1

        # also always update sofar, to ensure we do not 
        # conisder them gain
        # in other word it searched invalues that
        #they started before x and return the one with max end
        def find(x):
            nonlocal sofar
            end=-float("INF")  
            res=-1  
            for i in range(sofar,len(newRange)):
                sofar=i
                if  newRange[i][0]<=x:
                    if newRange[i][1]>end:
                        res=i
                        end=newRange[i][1]
                else:
                    break
            return res
        newRange=[]
      
      # to save the start and end of each tap that we choose  
      res=[(0,0)]
      
        # calculate the range of each tap
        for i,val in enumerate(ranges):
            start=i-val
            end=i+val
            newRange.append((start,end))
          
        # sort them based on starting point
        newRange.sort(key=lambda x:x[0]) 

        # if it srarts after zero return -1
        if newRange[0][0]>0:
            return -1
        
        sofar=0        
        while True:
            end=res[-1][1]
            index=find(end)
            print(index)
            if index==-1:
                return -1
            res.append(newRange[index])          
            if res[-1][1]>=n:
                 break
        # -1 because we added (0,0)
        return len(res)-1




        
        
