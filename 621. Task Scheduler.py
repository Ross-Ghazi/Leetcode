class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # way 1:using counter
        # freq=Counter(tasks)
        # maxfreq=freq.most_common(1)[0][1]        

        
        # way2: not using counter
        freq=collections.defaultdict(int)
        
        for item in tasks:
            freq[item]+=1
        maxfreq=0
        for val in freq.values():
            maxfreq=max (maxfreq, val)        
        
        
        
        # continue either way
        counter=0
        for k,v in freq.items():
            if v==maxfreq:  
                counter+=1
        
        res=(maxfreq-1)*(n+1)+counter        
        
        
        
        return max(len(tasks), res)
