#121. Best Time to Buy and Sell Stock
# Dec 11, 2020
#By Rouzbeh
#No refernce used. However to find max subarray I used this link before:
# https://www.youtube.com/watch?v=kqQnhBljXok&t=5s&ab_channel=RickyCho

def  maxProfit(prices):

    dif=[0]*(len(prices)-1)
    for i in range(len(prices)-1):
      dif[i]=prices[i+1]-prices[i]

    maxSum=0
    CurSum=0
    for i in range(len(dif)):
        CurSum=max(dif[i],CurSum+dif[i])
        maxSum=max(maxSum,CurSum)
    return maxSum

nums = [7,1,5,3,6,4]
print(maxProfit(nums))



