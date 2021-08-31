"""

15. 3Sum
Dec 10, 2020

https://www.youtube.com/watch?v=erEHQO0xljc

you can not delete the duplicates of nums because them for example [0,0,0] will be zero.
you cannot break because it does not work for exampel for [[0,0,0,0,0,0]

"""

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        k = len(nums) - 1
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            comp = -nums[i]
            while j < k:
                if (nums[j] + nums[k]) == comp:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif (nums[j] + nums[k]) < comp:
                    j = j + 1
                else:
                    k -= 1
        return res

a=Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))
