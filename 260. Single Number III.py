class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=[]
        map=collections.defaultdict(int)
        for i in range (len(nums)):
            temp=nums.pop()
            map[temp]+=1
        for key, val in map.items():
            if val==1:
                res.append(key)
        return res
