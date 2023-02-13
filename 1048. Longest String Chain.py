class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len) # or words.sort(key=lambda x:len(x))
        dp=defaultdict(int)       
        res=0        
        for word in words:
            temp=1            
            for x in range(len(word)):
                newWord=word[:x]+word[x+1:]
                
                temp=max(temp,dp[newWord]+1)
            dp[word]=temp
            res=max(res,temp)
            
        return res
        
