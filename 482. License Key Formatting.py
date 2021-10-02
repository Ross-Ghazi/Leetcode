class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res=0
        def dfs(root):
            if root==None:
                return 0
            cur=root
            l,r=0,0
            while cur!=0:
                cur=cur.left
                l+=1
            cur=root
            while cur!=0:
                cur=cur.
                r+=1
            if r==l:                
                res+=(2**l)-1
                
        dfs(root)
        return res
    
