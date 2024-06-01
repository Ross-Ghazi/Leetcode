# method 1, easy but slower O(n^2)
#https://www.youtube.com/watch?v=cjWnW0hdF1Y&ab_channel=NeetCode
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=len(nums)
        r=[1]*l
        for i in range(l-2,-1,-1):
            for j in range(i+1,l):
                if nums[i]<nums[j]:
                    r[i]=max(r[i], r[j]+1)
        return max(r)

# method 2, harder but faster  O(nlogn)
#https://www.youtube.com/watch?v=0wT67DOzqBg&ab_channel=KacyCodes
import bisect
class Solution:
    def lengthOfLIS(self, nums):
        piles = []        
        for num in nums:
            index = bisect.bisect_left(piles, num)
            if index == len(piles):
                piles.append(num)
            else:
                piles[index] = num        
        return len(piles)
# or if you do not want to use bisect
class Solution:
    def lengthOfLIS(self, nums):
        # find the leftmost position in a sorted list where a given number can be inserted to maintain the sorted order.
        def binary_search_left(piles, num):
            lo, hi = 0, len(piles)
            while lo < hi:
                mid = (lo + hi) // 2
                if piles[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid-1
            return lo
        piles = []        
        for num in nums:
            index = binary_search_left(piles, num)
            if index == len(piles):
                piles.append(num)
            else:
                piles[index] = num
        
        return len(piles)


