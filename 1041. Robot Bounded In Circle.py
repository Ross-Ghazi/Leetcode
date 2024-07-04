class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        movement=[0,0,0,0]
        index=0
        for inst in instructions:
            if inst=="G":
                movement[index]+=1
            elif inst=="R":
                index+=1
            else:
                index-=1
            if index>3:
                index-=4
            elif index<0:
                index+=4
        if (movement[0]!=movement[2] or movement[1]!=movement[3]) and index==0:
            return False
        return True
        
        






class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        s=instructions+instructions+instructions+instructions        
        ins=[0]*4    #index[0]=north, index[1]=east, etc ..
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
