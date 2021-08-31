#121. Best Time to Buy and Sell Stock

# June 2021

#No refernce used. But here is on link, do what exactly what I did:
# https://www.youtube.com/watch?v=I7KXD2OGDRQ&ab_channel=SaiAnishMalla
# another methosd is two pointef:
# https://www.youtube.com/watch?v=1pkOgXD63yU&ab_channel=NeetCode
def maxProfit(prices):
        if len (prices)==1:
            return 0
        mini=prices[0]
        maxProf=0
        for i in range(1,len(prices)):
            maxProf=max(maxProf,prices[i]-mini)
            mini=min(prices[i],mini)         
        return maxProf
            
            
# Dec 11, 2020
#No refernce used. However to find max subarray I used this link before:
# https://www.youtube.com/watch?v=kqQnhBljXok&t=5s&ab_channel=RickyCho

def  maxProfit2(prices):

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



