class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
          
        len1=len(nums1)
        len2=len(nums2)
        if len1==0 and len2==0:
            return 0    
        if len1>len2:
            nums1,nums2,len1,len2=nums2,nums1,len2,len1

        if len1==0:
            if len2%2 != 0:
                return nums2[len2//2]        
            return (nums2[len2//2]+nums2[len2//2-1])/2

        l=0
        r=len1-1
        while True:
            mid1=(l+r)//2
            mid2=(len1+len2)//2-(mid1+1)-1

            leftNum1=nums1[mid1] if mid1>=0 else -float ("INF")
            rightNum1=nums1[mid1+1] if mid1+1<len1 else float ("INF")
            leftNum2=nums2[mid2] if mid2>=0 else -float ("INF")
            rightNum2=nums2[mid2+1] if mid2+1<len2 else float ("INF")

            if leftNum1<=rightNum2 and leftNum2<=rightNum1:

                        if (len1+len2)%2==0:
                            return 0.5*(max(leftNum1,leftNum2)+min(rightNum1, rightNum2))
                        else:
                            return min(rightNum1, rightNum2)           

            elif leftNum1>rightNum2:
                       r=mid1-1 
            else:
                        l=mid1+1
