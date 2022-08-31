# refer to 907. Sum of Subarray Minimums
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        resmin,resmax=0,0
        numsmin=[-float("INF")]+nums+[-float("INF")]
        numsmax=[float("INF")]+nums+[float("INF")]
        stackmin,stackmax= [],[]
        for i,n in enumerate(numsmin):
            while stackmin and numsmin[stackmin[-1]]>n:                
                temp=stackmin.pop()            
                resmin+=numsmin[temp]*(temp-stackmin[-1])*(i-temp)
            stackmin.append(i)
        for i,n in enumerate(numsmax):     
            while stackmax and numsmax[stackmax[-1]]<n:                
                temp=stackmax.pop()       
                resmax+=numsmax[temp]*(temp-stackmax[-1])*(i-temp)
            stackmax.append(i)
        return resmax-resmin
        
