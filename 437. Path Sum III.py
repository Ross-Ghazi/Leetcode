# I made a vido on that
# https://www.youtube.com/watch?v=uZzvivFkgtM&ab_channel=CodeAndCoffee
# https://www.youtube.com/watch?v=HpqPcpP9uVQ&ab_channel=RickyCho
# use same concept as leetcode 560

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count=0
        compl=collections.defaultdict(int)
        compl[0]=1
        def dfs(node, currentSum=0):
            nonlocal count,compl
            if node==None:
                return
            currentSum+=node.val          
            count+=compl[currentSum-sum]            
            compl[currentSum]+=1
            dfs(node.left,currentSum)
            dfs(node.right,currentSum)
            compl[currentSum]-=1
        
        
        
        dfs(root)
        return count
