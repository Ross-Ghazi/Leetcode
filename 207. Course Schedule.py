class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        table={}
        visited=set()
        for course in prerequisites:
            if course[0] not in table:
                table[course[0]]=[course[1]]
            else:
                 table[course[0]]=table[course[0]]+[course[1]]
        
        def check(course):
            if course in visited:
                return False
            if course not in table:
                return True
            
            visited.add(course)
            for pre in table[course]:
                 res=check(pre)
                 if res == False:
                    return False
            visited.remove(course)
            table[course]=[]
            return True
            
        
        
        for course in table:            
            res=check(course)
            if res == False:
                return False
                
        return True
