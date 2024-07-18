class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq=defaultdict(list)
        for c,p in prerequisites:
            preq[c].append(p)
        seen=set()
        res=[]
        cycle=set()
        isCycle=False
        def dfs(course):
            nonlocal isCycle
            if isCycle==True or course in seen:
                return 
            if course in cycle :
                isCycle=True
                return
            cycle.add(course)
            for c in preq[course]:
                dfs(c)
            seen.add(course)
            res.append(course)
            cycle.remove(course)
        for c in range(numCourses):
            dfs(c)        
            if isCycle:
                return []
        return res


