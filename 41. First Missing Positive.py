"""By Rouzbeh
   2020-12-03
  Missing Smallest Positive Number?
You are given an unsorted array with both positive and negative elements. You have to find the smallest positive number missing from the array in O(n) time using constant extra space. You can modify the original array.
Examples
 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 https://youtu.be/-lfHWWMmXXM


  """

class solution:
    def firstmissingnumber (self, nums):
        n=len(nums)
        for i in range(n):
            correcPosition=nums[i]-1
            while num[i]>=1 and num[i]<n and num[i] !=correcPosition
                num[i], num[correcPosition]=num[correcPosition], num[i]
                correcPosition = nums[i] - 1

        for i in range(n):
            if num[i]<>i+1 return i+1

