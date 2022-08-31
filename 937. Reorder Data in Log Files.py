class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sortFunction(item):
            header,item=item.split(" ",1)           
            return item,header         
        
        letterArr=[]
        digitArr=[]             
        
        for item in logs:
            # if (str(item.split(" ")[1])[0]) in "0123456789":
            if (str(item.split(" ")[1])[0]).isdigit():
                digitArr.append(item)
            else:
                letterArr.append(item)              
    
        letterArr.sort(key=sortFunction)        
        return letterArr+digitArr
