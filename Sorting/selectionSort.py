"""
Implementation of selection sort algorithm

"""


def selectionSort(alist):
    n = len(alist)

    for i in range(0, n):
        min = i
        for j in range (i+1, n):
            if  alist[min] > alist[j]:
                min = j
        alist[i],alist[min] = alist[min],alist[i]

a = [1,5,3,2,0]
alist = [54,26,93,17,77,31,44,55,20]

selectionSort(alist)
selectionSort(a)

print(alist)
print(a)
