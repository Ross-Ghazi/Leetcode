
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
class Solution(object):
    def longestPalindrome(self, s):        
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res      
        
    def helper(self,s,l,r):        
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]
            
#######################################################
#above method is easier.
# 5. Longest Palindromic Substring
# Dec 14, 2020
# ref: https://www.youtube.com/watch?v=y2BD4MJqV20&t=2s&ab_channel=NickWhite
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0: return
        if len(s) == 1: return s
        max_maxi=0
        def expand(index):
                left=right=index
                while left>=0 and right<=len(s)-1:
                    if s[left] != s[right]:
                        break
                    left-=1
                    right += 1
                start=left+1
                end  = right-1
                maxi=end-start+1

                left =index
                right=index+1
                while left >= 0 and right <= len(s) - 1:
                    if s[left]!=s[right]:
                        break
                    left -= 1
                    right += 1

                start2 = left + 1
                end2 = right - 1
                maxi2 = end2 - start2 + 1
                if maxi>=maxi2:
                    return start, end,maxi
                else:
                    return start2, end2, maxi2

        for index in range(len(s)):
            a,b,maxi=expand(index)
            if maxi>max_maxi:
                res=s[a:b+1]
                max_maxi=maxi
        return res
a=Solution()
print(a.longestPalindrome("babad"))
