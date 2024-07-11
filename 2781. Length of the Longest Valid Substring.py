class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden=set(forbidden)
        l=0
        res=0
        for r in range(len(word)):
            for j in range(r,max(l-1,r-10),-1):
                if word[j:r+1] in forbidden:
                    l=j+1
                    break
            res=max(res,r-l+1)
        return res
