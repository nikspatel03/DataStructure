"""

Implementation of recursive binary search algorithm

"""


def binarySearch(arr, item):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2

        if arr[mid] == item:
            return True
        else:
            if arr[mid] > item:
                return binarySearch(arr[:mid], item)
            else:
                return binarySearch(arr[mid+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
