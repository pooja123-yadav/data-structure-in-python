def lenOfLongSubarr (arr, n, k):
    max_length = 0
    for i in range(n):
        currsum = 0
        for j in range(i,n):
            currsum  += arr[j]
            if currsum == k:
                max_length =  max(max_length, j-i+1)

    return max_length


def OptmizedSolution(arr, n, k):
    max_length = 0
    sum = 0
    for i in range(n):
        pass

    return max_length


arr = [10, 5, 2, 7, 1, 9]
k = 15
print(lenOfLongSubarr(arr,6,k))
