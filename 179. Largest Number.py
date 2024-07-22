class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i]=str(n)
   
        def compare(n1,n2):           
            if n1+n2>n2+n1: #they are string
                return -1 # case when we want n1 first
            else:
                return 1 # case when we want n2 first
                
        nums=sorted(nums,key=cmp_to_key(compare))
        nums="".join(nums)         
        return str(int(nums)) # input [0,0,0] the result should be "0" not "000"
