"""By Rouzbeh
   2020-12-02
  pascall_Triangle
  https://leetcode.com/problems/pascals-triangle/
  https://www.youtube.com/watch?v=icoql2WKmbA&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=2&ab_channel=NickWhite
  regular_Triangle1. Before we solve that we should be able to maka list such that for n=4:
    [[1],
    [1, 1],
    [1, 1, 1],
    [1, 1, 1, 1]]

    regular_Triangle2. Before we solve that we should be able to maka list such that for n=4:
    [[1],
    [1, 1], [1, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0, 1]]


  """
def regular_Triangle(r): # see on top comments, regular_Triangle1
    if r==1: return (1)
    arr=[]
    for i in range(0,r):
        arr.append([1])
        for j in range (0,i):
                arr[i].append(1)
    return (arr)


def regular_Triangle_alter(r):
    arr=[[1]]
    for i in range (1,r):
        arr.append([1])
        for j in range (0,i):
            arr[i].append(1)
    return arr

def regular_Triangle2(r):  # see on top comments, regular_Triangle2
    if r==1: return (1)
    arr=[]
    for i in range(0,r):
        arr.append([1])
        for j in range (0,i):
                if j==i-1:
                    value = 1
                else:
                    value=0
                arr[i].append(value)
    return (arr)


def pascall_Triangle(r):  # see on top comments, regular_Triangle2
    if r==1: return (1)
    arr=[]
    for i in range(0,r):
        arr.append([1])
        for j in range (0,i):
                if j==i-1:
                    value = 1

                else:
                    value=arr[i-1][j]+arr[i-1][j+1]    # as it will start from 0 rather than 1
                arr[i].append(value)
    return (arr)

def pascall_Triangle2(r):  # see on top comments, regular_Triangle2
    if r==1: return (1)
    arr=[[1]]
    for i in range(1,r):
        arr.append([1])
        for j in range (0,i):
                if j==i-1:
                    value = 1

                else:
                    value=arr[i-1][j]+arr[i-1][j+1]    # as it will start from 0 rather than 1
                arr[i].append(value)
    return (arr)





print(regular_Triangle(4))
print(regular_Triangle_alter(4))
print(regular_Triangle2(4))
print(pascall_Triangle(4))
print(pascall_Triangle2(4))