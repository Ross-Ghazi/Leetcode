# no refernce was used
class Solution:
    def intToRoman(self, num: int) -> str:
        res=[]
        #more than 1000 
        temp=num//1000
        for i in range(temp):               
                res+="M"    
        

        #up tp 1000   
        num=num %1000
        if num>=900:
              res+="CM"
              num-=900
        else:
            temp=num//500
            for i in range(temp):               
                res+="D"    
      
        #up tp 500   
        num=num %500
        if num>=400:
              res+="CD"
              num-=400
        else:
            temp=num//100
            for i in range(temp):               
                res+="C"
 
        #up tp 100
        num=num %100
        if num>=90:
              res+="XC"
              num-=90
        else:
            temp=num//50
            for i in range(temp):               
                res+="L"

        #up tp 50   
        num=num %50
        if num>=40:
              res+="XL"
              num-=40
        else:
            temp=num//10
            for i in range(temp):               
                res+="X"
        #up to 10
        num=num %10
        if num==9:
                res+="IX"
                num-=9
        else:
            temp=num//5
            for i in range(temp):
                res+="V"

        # up tp 5 
        num=num %5
        temp=num//1
        for i in range(temp):
            if num==4:
                res+="IV"
                break
            else:
                res+="I"
        num=num %10
        
        res="".join(res)
        return res


a= Solution()
print (a.intToRoman(1994))


        
