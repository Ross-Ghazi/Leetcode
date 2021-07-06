# first read BFS algorithm
# https://www.youtube.com/watch?v=h9iTnkgv05E&ab_channel=NeetCode
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dic=defaultdict(list)
        visited={}
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                temp=word[:i]+"*"+word[i+1:]
                dic[temp]+=[word]
        que=deque()
        que.append(beginWord)
        visited[beginWord]=True
        res=1
        while que:
            for j in range(len(que)):
                word=que.popleft()
                if word==endWord:
                    return res
                for i in range(len(word)):
                    temp=word[:i]+"*"+word[i+1:]
                    for item in dic[temp]:
                        if item not in visited:
                            visited[item]=True
                            que.append(item)
            res+=1
        return 0    
            
