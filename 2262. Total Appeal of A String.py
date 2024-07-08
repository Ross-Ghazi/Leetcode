# same idea as 828
# my own video


class Solution:
    def appealSum(self, s: str) -> int:
        # "abbca" 
        # first b contribution:
        # ab,abb,abbc,abbca,b,bb,bbc,bbca->8 
        # left options : a, _ ->2
        # right options : _,b, bc ,bca->4
        # options: left*right=8
        # left=i-prev_occurance 
        # right before for 828:=item[i+1]-item[i]
        # right now for 2262 as it can go all the way to the end: right=len(s)-item[i]
        dic={}
        for i,c in enumerate(s):
            if c in dic:               
                dic[c].append(i)       
            else:
                dic[c]=[-1,i]    #will add -1 and len(s) to the dic
        res=0
        for item in dic.values():
            
            for i in range(1,len(item)):
                left=item[i]-item[i-1]
                right=len(s)-item[i]
                res+=left*right
        return res
