
#31. Next Permutation
#ref:
#https://www.youtube.com/watch?v=9xT2Xzlo4i4&t=41s
#input[1,7,9,9,8,3]
# step 1: [1,7,9,9,8,3] Find i=2 j=i-1=1
# step 2:[1,7,3,8,9,9] reverse i and after
# step 3: [1,8,3,7,9,9] replace 8 and 7


class Solution:
    def nextPermutation(self, nums):
            # step 1:      
            find=False
            for i in (range(len(nums)-1,0,-1)):
                if nums[i]>nums[i-1]:
                    find =True
                    break
            if find==False:
                return nums.reverse()
            #in Leetcode, nums=.... will not work because it should be changes in palce
            #when you say nums=.... it will create a new address and will not change the  refence values
            # step 2:
            nums[:]=nums[:i]+nums[:i-1:-1]
            j=i-1
            # step 3:
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
