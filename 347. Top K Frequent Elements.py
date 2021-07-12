# two ways:
# https://www.youtube.com/watch?v=YPTqKIgVk-k&ab_channel=NeetCode

class Solution:
    def topKFrequent(self, nums, k):
        res=[]
        Count = Counter(nums)                  
        # bucket=[[]]*(len(nums)+1)  # wrong 
        bucket=[[] for _ in range(len(nums)+1)]        
        for n,freq in Count.items():          
            bucket[freq]+=[n]         
        for i in range(len(bucket)-1,-1,-1):
            if bucket !=[]:
                res+=bucket[i]
                if len (res)>=k:
                    return res
                  
   # second way
    def topKFrequent2(self, nums, k):
        res=[]
        Count = Counter(nums)  
        Count1 = Counter(nums).most_common(k)        
        for item in Count1:
            res.append(item[0])       
        return res          
