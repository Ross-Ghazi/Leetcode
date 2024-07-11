class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq=collections.Counter(s).most_common()
        res=0
        for i in range(len(freq)):
            f=freq[i][1]
            res+=f*(i//9+1)
        return res

       
