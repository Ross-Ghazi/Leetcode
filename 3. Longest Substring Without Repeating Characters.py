"""
3. Longest Substring Without Repeating Characters

Saw the algorithm from the solution section , but the code is mine
"""
def lengthOfLongestSubstring(s):
    dic={}
    ans=0
    i=j=0
    for j,c in enumerate(s):
        if c  in dic:
            i=max(i,dic[c]+1)
        ans = max(ans, j - i + 1)
        dic[c] = j
    return ans
print(lengthOfLongestSubstring("tmmzuxt"))
