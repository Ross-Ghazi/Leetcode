class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict=set(wordDict)
        res=[]
        cur=""
        def dfs(i):
            nonlocal cur
            if i==len(s):
                cur=cur.strip()
                res.append(cur)
                return
            for j  in range(i,len(s)):
                word=s[i:j+1]
                if word in wordDict: 
                    temp=cur                                 
                    cur=cur+" "+word                    
                    dfs(j+1)
                    cur=temp                  

        dfs(0)
        return res

# or

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict=set(wordDict)
        cur=[]
        res=[]
        def helper(i):
            if i==len(s):                
                res.append(" ".join(cur))
                return
            for j in range(i,len(s)):
                word=s[i:j+1]
                if word in wordDict:
                    cur.append(word)
                    helper(j+1)
                    cur.pop()
        helper(0)
        return res
