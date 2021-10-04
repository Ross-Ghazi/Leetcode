class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        remove="!?',;."
        for c in remove:
            paragraph=" ".join(paragraph.split(c))             
       
        banned.append("")        
        
        for i in range(len(banned)):
            banned[i]= banned[i].lower()
        arr=paragraph.split(" ")
        print(arr)
        
        count=collections.Counter(arr).most_common()
        print(count)
        s=iter(count)        
        while True:
            word,freq=next(s)   
            print(word)
            if word not in banned:
                return word
        
        
