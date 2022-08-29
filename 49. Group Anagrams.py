#no ref was used. 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        res=[]
        for word in strs:
            key=list(word)
            key.sort()
            dic[tuple(key)].append(word)            
        return dic.values()
            
        
        
