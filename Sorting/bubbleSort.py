"""

Implementation of BubbleSort algorithm

"""

def bubbleSort(alist):
    # calculate the length of alist
    n = len(alist)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]


a = [1,5,3,2,0]
alist = [54,26,93,17,77,31,44,55,20]

bubbleSort(alist)
bubbleSort(a)

print(alist)
print(a)
