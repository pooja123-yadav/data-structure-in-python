def moveNegativeToBeginning(nums,n):

    j = 0
    for i in range(n):
        if nums[i] < 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums

def moveNegativeToEnd(nums,n):

    j = 0
    for i in range(n):
        if nums[i] >= 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9 ]

print(moveNegativeToBeginning(arr, n=9))
print(moveNegativeToEnd(arr, n=9))

