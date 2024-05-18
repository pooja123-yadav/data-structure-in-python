def rotateArrayToLeft(nums, k):
    n = len(nums)
    if k == n:
        return nums
            
    if k > n:
        k = k % n

    temp = nums[0:k]
    for i in range(k,n):
        nums[i-k] = nums[i]

    # for j in range(k):
    #     nums[j+k+1] = temp[j]   

    i = n-1
    while i >= n-k and temp:
        nums[i] = temp.pop()
        i -= 1

    return nums

def RotateLeftApproach2(arr,k):
    n = len(nums)
    if k == n:
        return nums
            
    if k > n:
        k = k % n

    reverseArray(arr,0,k-1)
    reverseArray(arr,k,n-1)
    reverseArray(arr,0,n-1)

    return arr
    

def reverseArray(arr, start, end):
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


nums = [1,2,3,4,5,6,7]
k = 3
# print(rotateArrayToRight(nums, k))
# print(rotateArrayToLeft(nums, k))
print(RotateLeftApproach2(nums, k))