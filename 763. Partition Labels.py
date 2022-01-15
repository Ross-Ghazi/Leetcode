#No refernce
    #look at example 1:  ababcbacadefegdehijhklij
        # ababcbaca   defegde          hijhklij
        # 012345678   9101112131415    1617181920212223
        #[8-0+1]      [15-9+1]          #[23-16+1]
        # we wan to find start and end for each part, first start=0,end=8
        # then start=15, end=9, etc...
        #when to find start and end is when i>end
        # then we set start as i and end as end[c]
        # because the loop does not take the last one we add it manually at the end
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #keep end index of each letter in a dic
        dic=dict()
        for i,c in enumerate(s):
            dic[c]=i
        
        res=[]        
        start=0
        end=0       
        for i,c in enumerate(s):           
            if i>end:
                res.append(end-start+1)
                start=i
                end=dic[c]
            end=max(end,dic[c])
        res.append(len(s)-start)            
        return res
    
        

# # no ref was used
# # the idea behind leetcode 53 (Merge Intervals) was used here.
# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#       # first for each letter we put its first appearnace and last appearance in a dic
#       dic={}        
#         for i,c in enumerate(s):            
#             if c in dic:
#                 l,r=dic[c]
#                 r=i
#                 dic[c]=[l,r]
#             else:
#                 dic[c]=[i,i]
#         # we do not care about alphabaet or keys we just care about values:   
#         li=list(dic.values())
        
#         # using the idea behind leetcode 53 (Merge Intervals) we know li is already sorted by first appearance and we will find the merge intervals
        
#         res=[li[0]]
#         for i in range(1,len(li)):
#             l1,r1=res[-1]
#             l2,r2=li[i]
#             if l2<=r1:
#                 res[-1][1]=max(r1,r2)
#             else:
#                 res.append([l2,r2])
#         # the question is asking for length of each interval
#         res1=[]
#         for item in res:
#             res1.append(item[1]-item[0]+1)
#         return res1
        
        
        
        
            
                
        
