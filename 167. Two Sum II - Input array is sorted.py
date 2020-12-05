"""
Two sum II
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


Solution:
Two methos used:
1. Since the array is sorted we can use pointer.
2. General for using hashtable and dic

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).
https://www.youtube.com/watch?v=sAQT4ZrUfWo&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=5&ab_channel=NickWhite

"""


class Solution:
    # two-pointer
    def twoSum1(self, numbers, target):
        i,j=0,len(numbers)-1
        while(i<j):
            sum=numbers[i]+numbers[j]
            if sum<target:
                i+=1
            elif sum>target :
                j-=1
            else:
                return [i+1,j+1]  #+1 since the question says index start from 1

    # Hashtable/dic
    def twoSum2(self, numbers, target):
        dic={}
        for i, num in enumerate(numbers):
            if target-num not in dic:
                dic[num]=i
            else:
                return [dic[target-num]+1, i+1]

  # Hashtable/dic
    def twoSum3(self, numbers, target):
        dic={}
        for i,num in enumerate(numbers):
            comp=target-num
            if num  not in dic:
                dic[comp]=i
            else:
                return [i+1, dic[comp]+1]


a=Solution()
output=a.twoSum1([2,7,11,15],9)
print(output)
output=a.twoSum2([2,7,11,15],9)
print(output)
output=a.twoSum3([2,7,11,15],9)
print(output)