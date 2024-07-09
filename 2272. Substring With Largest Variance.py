# https://leetcode.com/problems/substring-with-largest-variance/solutions/2041108/python3-enumerate-all-a-b-combinations-and-do-maximum-subarray/
class Solution:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        for a,b in itertools.permutations(counter,2):
            max_subarray=0
            has_a,has_b = False,False
            remain_a,remain_b = counter[a],counter[b]
            for ch in s:
                if ch!=a and ch!=b:
                    continue
                # consider "xyy", and a=y and b=x 
                # we get to y, max_subarray=-1 
                # but we cannot make a new subarray, becase there is no
                #subarray after, but at the end it will get +1.
                if max_subarray<0 and remain_a!=0 and remain_b!=0:
                    max_subarray=0
                    has_a,has_b = False,False
                if ch==a: 
                    max_subarray+=1
                    remain_a-=1
                    has_a = True
                elif ch==b: 
                    max_subarray-=1
                    remain_b-=1
                    has_b = True
                if has_a and has_b:
                    res = max(res, max_subarray)
        return res
