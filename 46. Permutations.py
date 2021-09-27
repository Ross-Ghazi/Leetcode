class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]   
        def dp (rem,path):
            if len(rem)==0:
                    res.append(path)                   
            for i in range(len(rem)):            
                dp(rem[:i]+rem[i+1:] ,path+[rem[i]])


        dp(nums,[])

        return res
