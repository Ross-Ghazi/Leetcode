#bottom-up
# simiar to question 97
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1=text1
        s2=text2
        col=len(s1)+1
        row=len(s2)+1
        dp=[[0]*(col) for _ in range(row)]
        
        for r in range(row-2,-1,-1):# row-2=len(s2)-1
            for c in range(col-2,-1,-1): # col-2=len(s1)-1
                print(r,c)
                if s1[c]==s2[r]:
                    dp[r][c]=dp[r+1][c+1]+1
                else:
                    dp[r][c]=max(dp[r+1][c],dp[r][c+1])                      
        return dp[0][0]
    
        

#--------------ignore below----------------------------#

# 1143. Longest Common Subsequence
# two methods: recursive (for some reason slow even when I use lru_cache
# second method is buttom up and dynamic programming table
# https://www.youtube.com/watch?v=ASoaQq66foQ&ab_channel=BackToBackSWE
# https://www.youtube.com/watch?v=sSno9rV8Rhg&t=1014s&ab_channel=AbdulBari
# longestCommonSubsequence2 and 3 are the same. However, I added 3 later because it is eaiser to implement and undersantd. 
# The only difference is how to treat the boundry

class Solution:
    #recursive does not ru for really long string, giving error
    from functools import lru_cache
    @lru_cache(None)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)==0 or len(text2)==0:
            return 0
        if text1[0]==text2[0]:
            return 1+self.longestCommonSubsequence(text1[1:],text2[1:])
        else:
            return max(self.longestCommonSubsequence(text1[1:],text2),
                       self.longestCommonSubsequence(text1,text2[1:]))

    #buttom up
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        table=[[0]*(len(text1)+1) for i in range(len(text2)+1)]

        for i in range(1,len(text2)+1):
             for j in range(1,len(text1)+1):
                 if text1[j-1]==text2[i-1]:
                      table[i][j]=1+table[i-1][j-1]
                 else:
                      table[i][j] =max(table[i-1][j],table[i][j-1])
        return table[len(text2)][(len(text1))]
     #buttom up easier to understand 
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        text1="0"+text1
        text2="1"+text2
        colMax=len(text1)
        rowMax=len(text2)
        table=[[0]*colMax for _ in range(rowMax)]      
       
        for i in range(1,rowMax):
            for j in range(1,colMax):
                if text1[j]==text2[i]:
                    table[i][j]=table[i-1][j-1]+1
                else:
                    table[i][j]  =max (table[i][j-1], table[i-1][j])
        return table[-1][-1]





a=Solution()

print(a.longestCommonSubsequence2("bsbininm","jmjkbkjkv"))

print(a.longestCommonSubsequence2("fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny",
"nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan"))
