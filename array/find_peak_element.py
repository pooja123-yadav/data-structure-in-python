def findPeakElement(arr):
    n = len(arr)
    ans = []
    # for i in range(1,n-1):
    #     if arr[i-1] < arr[i] > arr[i+1]:
    #         ans.append(arr[i])

    # return ans

    s, e = 0, n-1

    while s<e:
        mid = s+ (e-s)//2

        if arr[mid] > arr[mid+1]:
            ans.append(arr[mid])
            e = mid
        else:
            s = mid + 1

    return ans

arr = [20, 25, 35, 51, 15, 45, 70, 5]

print(findPeakElement(arr))

