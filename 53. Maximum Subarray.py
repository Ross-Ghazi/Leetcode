#53. Maximum Subarray
# Dec 11, 2020
#By Rouzbeh
# https://www.youtube.com/watch?v=kqQnhBljXok&ab_channel=RickyCho
# https://www.youtube.com/watch?v=wnkZKar0UiM&ab_channel=GiuseppePicciano
#lower link put currentsom=0 rather than -inifnity  which is wrong because if all integers are negative
#it will not work. Solution:
# if curretsum<0 is same as max(currentsum, currentsum+num)

def maxSubArray(nums):
    currentSum=maxSum=-float("INF")
    for n in nums:
        currentSum=max(n,currentSum+n)
        if currentSum>maxSum: maxSum=currentSum
    return maxSum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))



