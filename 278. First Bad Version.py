"""
278. First Bad Version
Dec 9, by Rouzbeh
Did not use any reference.
"""
def isBadVersion(n):
    if n<5: return False
    else: return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 : return 1
        if isBadVersion(n) == False: return n
        if isBadVersion(1) == True: return 1
        def bSearch(min,max):
            mid=(min+max)//2

            if isBadVersion(mid) is True:
                if isBadVersion(mid-1) is False:
                    return mid
                else:
                    max=mid-1
            else:
                if isBadVersion(mid +1) is True:
                    return mid+1
                else:
                    min = mid + 1
            return bSearch(min,max)

        return bSearch(1,n)



a=Solution()
print(a.firstBadVersion(11))




