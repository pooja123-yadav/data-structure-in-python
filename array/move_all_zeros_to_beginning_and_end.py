def moveZerosToBeginning(nums,n):
    # non_zeros = []
    # for num  in arr:
    #     if num != 0:
    #         non_zeros.append(num)

    # i = n - 1

    # while non_zeros:
    #     arr[i] = non_zeros.pop()
    #     i -= 1

    # while i>= 0:
    #     arr[i] = 0
    #     i -= 1

    i = 0
    for j in range(n):
        if nums[j] == 0:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
    return nums

def moveZerosToEnd(nums,n):
    j = 0
    for i in range(n):
        if nums[i] != 0:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

    return nums  
    


arr = [1, 2, 3, 0, 0, 0, 0, 0, 0]

print(moveZerosToBeginning(arr, n=9))
print(moveZerosToEnd(arr, n=9))
