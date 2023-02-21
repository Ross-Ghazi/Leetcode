class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while True:
            if l>r:
                return -1
            mid = (l + r) // 2
            if nums[mid]==target:
                return mid
            
            #just to ensure we capture edge cases
            if nums[l]==target:
                return l          
            #just to ensure we capture edge cases
            if nums[r]==target:
                return r

            #if both target and nums[mid] are on the same side ( either left or right hand side) then
            # we can treat it as regular sorted array
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if (nums[mid] < target):
                    l = mid + 1
                elif (nums[mid] > target):
                    r = mid - 1               
            #target and nums[mid] are on different sides
            else:
                #target in left hand side, we do not care about right hand side
                #if we put <= here no need to have nums[l]==target and nums[r]==target consitions 
                if nums[0]<=target: 
                    r=mid-1
                else:
                    l=mid+1

        return -1
