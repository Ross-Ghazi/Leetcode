class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        s=instructions+instructions+instructions+instructions        
        ins=[0]*4    #index[0]=north, index[1]=west, etc ..
        index=0
        for c in s:
            if c=="G":                
                ins[index]+=1
            elif c=="L":
                index+=1
            else:
                index-=1
            
            if index>=4:
                index-=4
            elif index<0:
                index+=4
        if ins[0]==ins[2] and ins[1]==ins[3]:
            return True
        return False 
