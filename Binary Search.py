# RBinSearch and IBinSearch are Recursive and Iterative Binary Search  
# If target value is inside A they will retrun it.
# If target value is not inside A they will retrun previoius and next index of that that
# If target is less than A[0] it will return (-1,0).
# If target is more than A[max] it will return (max,max+1).

# Recursive Binary Search  
def RBinSearch(l,r): 
    if l>r:
        return r,l        
    mid=(l+r)//2
    if target==A[mid]:
        return mid    
    if target<A[mid]:
        # don not forget to have return
        return RBinSearch(l,mid-1)
    else:
        return RBinSearch(mid+1,r)
# Iterative Binary Search , exatly same as Recursive
def IBinSearch(l,r): 
    while True:
        if l>r:
            return r,l        
        mid=(l+r)//2
        if target==A[mid]:
            return mid
        if target<A[mid]:
            r=mid-1
        else:
            l=mid+1


def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


A=[0,1,2,3,4,5,6,7,8]
target=5.5
print(RBinSearch(0,len(A)-1))
print(IBinSearch(0,len(A)-1))
