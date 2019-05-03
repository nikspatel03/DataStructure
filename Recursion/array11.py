"""

Given an array of ints, compute recursively the number of times that the
value 11 appears in the array. We'll use the convention of considering only
the part of the array that begins at the given index. In this way, a recursive
call can pass index+1 to move down the array. The initial call will pass in
index as 0.


array11([1, 2, 11], 0) → 1
array11([11, 11], 0) → 2
array11([1, 2, 3, 4], 0) → 0

"""

def array11(nums, index):
    if index == len(nums):
        return 0
    else:
        return 1 + array11(nums, index + 1) if nums[index] == 11 \
            else array11(nums, index + 1)

print(array11([1, 2, 11], 0))
print(array11([11, 11], 0))
print(array11([1, 2, 3, 4], 0))

print(array11([1, 11, 3, 11, 11], 0))
