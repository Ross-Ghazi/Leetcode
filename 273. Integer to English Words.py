class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
       
        
        def helper(n):
            if n<20:
                return lessThan20[n]
            
            if n <100:
                nLeft=n//10
                nRight=n%10                               
                return (tens[nLeft]+" "+lessThan20[nRight]).strip()
        
            if n <1000:
                nLeft=n//100
                nRight=n%100                              
                return (lessThan20[nLeft]+" Hundred "+helper(nRight)).strip()
        
            if n<1000*1000:
                nLeft=n//1000
                nRight=n%1000
                return (helper(nLeft)+" Thousand "+helper(nRight)).strip()
                
            if n<1000*1000*1000:
                nLeft=n//(1000*1000)
                nRight=n%(1000*1000)
                return (helper(nLeft)+" Million "+helper(nRight)).strip()
    
        
            if n<1000*1000*1000*1000:
                nLeft=n//(1000*1000*1000)
                nRight=n%(1000*1000*1000)
                return (helper(nLeft)+" Billion "+helper(nRight)).strip()
        
        return helper(num)
