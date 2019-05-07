"""

Implementation of recursive binary search algorithm

"""

"""
## This is still O(n) because spliting the list takes O(n) runtime
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
"""
## O(log n) version  using the index approach
def binarySearch(alist, item):
    return binarySearcHelper(alist, item, 0, len(alist) - 1)

def binarySearcHelper(alist, item, low, high):
    if low > high:
        return False
    else:
        mid = low + (high - low) // 2

        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binarySearcHelper(alist, item, low, mid - 1)
        else:
            return binarySearcHelper(alist, item, mid + 1, high)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
