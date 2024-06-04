#https://www.youtube.com/watch?v=s6ATEkipzow&ab_channel=NeetCode
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def return(root,maxAllowed,minAllowed):
            if not root:
                return True
            if root.val>=maxAllowed or root.val<=minAllowed:
                return False

            return return(root.left ,root.val,minAllowed) and return(root.right ,maxAllowed,root.val)

        return return(root,float("inf"),-float("inf"))
