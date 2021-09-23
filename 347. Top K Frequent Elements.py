# three methods: counter .most_common, heap and bucket sorting

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # first Method, Counter and most_common
        # col=Counter(nums).most_common(k)
        # res=[]
        # for number,kiri in col:
        #     res.append(number)
        # return res
        
        # # second  Method, heap
        # freq=defaultdict(int)
        # for n in nums:
        #     freq[n]+=1
        # res=[]
        # for n,fr in freq.items():
        #     if len(res)<k:
        #         heapq.heappush(res, (fr,n))
        #     else:
        #         heapq.heappushpop(res, (fr,n))     
        # return [n for fr,n in res]
        
        
        # # Third  Method, Bucket sorting
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        bucket=[[] for _ in range(len(nums)+1)]                      
        for num,fre in freq.items():
            bucket[fre].append(num)
        res=[]
        while len(res)<k and bucket!=[]:
            numlist=bucket.pop()            
            if numlist:
                for item in numlist:
                    res.append(item)
        return res
        
        
        
