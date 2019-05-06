"""

Implementation of QuickSort algorithm

"""


def quickSort(arr):
    quickSortHelper(arr, 0, len(arr)-1)

def quickSortHelper(arr, first, last):
    if first < last:
        splitPoint = partition(arr, first, last)

        quickSortHelper(arr, first, splitPoint - 1)
        quickSortHelper(arr, splitPoint + 1, last)

def partition(arr, first, last):
    pivotValue = arr[first]

    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotValue:
            leftmark += 1

        while rightmark >= leftmark and arr[rightmark] >= pivotValue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark],arr[rightmark] = arr[rightmark],arr[leftmark]

    arr[first],arr[rightmark] = arr[rightmark],arr[first]

    return rightmark


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

a = [54,26,93]
alist = [54,26,93,17,77,31,44,55,20]

quickSort(alist)
quickSort(a)

print(alist)
print(a)
