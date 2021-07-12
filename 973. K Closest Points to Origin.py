class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for point in points:
            dist=(point[0]**2+point[1]**2)**0.5
            point.append(dist)
        points.sort(key=lambda i:i[2])
        
        for i in range(k): 
            point=points[i]
            temp=[point[0], point[1]]
            res.append(temp)
        
        return res    
        
#using heap ,better approach
# https://www.youtube.com/watch?v=rI2EBUEMfTk&ab_channel=NeetCode
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         res=[]
#         heap=[]
#         for point in points:
#             dist=(point[0]**2+point[1]**2)**0.5
#             heap.append([dist,point[0],point[1]])
                              
#         heapq.heapify(heap)
#         for _ in range(k):
#             a,x,y=heapq.heappop(heap)
#             res.append([x,y])        
#         return res    
        
