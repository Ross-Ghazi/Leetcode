# there are two ways
# heap and bucket, the issue with heap is then sorting base on alpahbet is harder
# simiar to 346

# my own method:

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter=collections.Counter(words)
        max_freq=counter.most_common()[0][1]
        dic=collections.defaultdict(list)
        for word,freq in counter.most_common():
            dic[freq].append(word)        
        freq=max_freq
        res=[]        
        while True:
            # we need this line to ensure if freq not in dic we add res with [] not partial_res from previous round
            partial_res=[]
            
            if freq in dic:
                partial_res=dic[freq]
                
                # sort will automatically sort string list based on alphabet
                partial_res.sort()           
            res+=partial_res
            if len(res)<k:              
                freq-=1                
            elif len(res)==k:
                return res
            else:
                return res[:k]
                
        


# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         res=[]
#         dic=collections.defaultdict(int)
#         for word in words:
#             dic[word]+=1
#         #bucket solution
#         bucket=[[] for _ in range(len(words)+1)]
#         for word,count in dic.items():
#                 bucket[count].append(word)
        
#         for i in range (len(words),-1,-1):
#                 temp=bucket.pop()
#                 temp.sort()
#                 if len(res)+len(temp)<k:
#                     res+=temp
#                 elif len(res)+len(temp)==k:
#                     res+=temp
#                     return res
#                 else:
#                     break
#         temp.reverse()
#         while True:
#             res.append(temp.pop())
#             if len(res)==k:
#                 return res
            
                
