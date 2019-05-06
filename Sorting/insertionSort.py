"""
Implementation of insertionSort

"""


def insertionSort(arr):

    n = len(arr)

    for i in range(1, n):
        j = i-1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key


a = [1,5,3,2,0]
alist = [54,26,93,17,77,31,44,55,20]

insertionSort(alist)
insertionSort(a)

print(alist)
print(a)
