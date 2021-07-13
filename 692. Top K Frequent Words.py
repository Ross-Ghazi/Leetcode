# there are two ways
# heap and bucket, the issue with heap is then sorting base on alpahbet is harder
# simiar to 346
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res=[]
        dic=collections.defaultdict(int)
        for word in words:
            dic[word]+=1
        #bucket solution
        bucket=[[] for _ in range(len(words)+1)]
        for word,count in dic.items():
                bucket[count].append(word)
        
        for i in range (len(words),-1,-1):
                temp=bucket.pop()
                temp.sort()
                if len(res)+len(temp)<k:
                    res+=temp
                elif len(res)+len(temp)==k:
                    res+=temp
                    return res
                else:
                    break
        temp.reverse()
        while True:
            res.append(temp.pop())
            if len(res)==k:
                return res
            
                
