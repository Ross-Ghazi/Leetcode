class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq=defaultdict(list)
        for c,p in prerequisites:
            preq[c].append(p)
        cycle=set()
        seen=set()
        def check(course):
            if course in seen:
                return True
            if course in cycle:
                return False
            cycle.add(course)
            for c in preq[course]:
                if not check(c):
                    return False
            cycle.remove(course)
            seen.add(course)
            return True
        for course in range(numCourses):
            if not check(course):
                return False
        return True

