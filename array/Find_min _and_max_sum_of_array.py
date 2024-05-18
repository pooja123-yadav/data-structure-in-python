def FindMinMaxSumArray(arr):
    sum = 0
    mini = float('inf')
    maxi = float("-inf")

    for num in arr:
        sum += num
        mini = min(mini, num)
        maxi = max(maxi, num)

    return sum-maxi, sum-mini

arr=[10, 9, 8, 7, 6, 5]
print(FindMinMaxSumArray(arr))

