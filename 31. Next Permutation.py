# By Rouzbeh on Dec 12
#31. Next Permutation
#ref:
#https://www.youtube.com/watch?v=9xT2Xzlo4i4&t=41s

class Solution:
    def nextPermutation(self, nums):
            find=False
            for i in (range(len(nums)-1,0,-1)):
                if nums[i]>nums[i-1]:
                    find =True
                    break
            if find==False:
                return nums.reverse()
            #in Leetcode, nums=.... will not work because it should be changes in palce
            #when you say nums=.... it will create a new address and will not change the  refence values
            nums[:]=nums[:i]+nums[:i-1:-1]
            j=i-1
            while i>0 and i<len(nums):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    # in reality Leetcode will not care about what you return it just
                    # care bout nums.
                    return nums
                i+=1
a=Solution()
nums=[2,3,1]
c=a.nextPermutation(nums)
print(c)