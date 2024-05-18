def RotateArrayToRight(nums, k):
    n = len(nums)
          
    if k > n:
        k = k % n

    if k == n:
        return nums

    temp = nums[n-k:n]

    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]

    for i in range(k):
        nums[i] = temp[i]


    return nums

def RotateRightApproach2(arr,k):
    n = len(nums)
    if k == n:
        return nums
            
    if k > n:
        k = k % n

    reverseArray(arr,n-k,n-1)
    reverseArray(arr,0,n-k-1)
    reverseArray(arr,0,n-1)

    return arr
    

def reverseArray(arr, start, end):
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


nums = [1,2,3,4,5,6,7]
k = 3
# print(RotateArrayToRight(nums, k))
print(RotateRightApproach2(nums, k))

# [4,3,2,1,7,6,5]
# [5,6,7,1,2,3,4]