def FindLargesstElement(arr):
    n = len(arr)
    maxi = arr[0]

    for i in range(1, n):
        maxi = max(maxi,arr[i])

    return maxi

def FindSecondLargestElement(arr):
    n = len(arr)
    maxi = arr[0]
    second_maxi = float("-inf")

    for i in range(1,n):
        if arr[i] > maxi:
            second_maxi = maxi
            maxi = arr[i]
        elif (arr[i] > second_maxi) and (arr[i] != maxi):
            second_maxi = arr[i]

    return second_maxi


def FindThirdLagestElement(arr):
    n = len(arr)
    if n < 3:
        return False
    
    first = float("-inf")
    second = float("-inf")
    third = float("-inf")

    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num

    return third

arr = [12, 35, 1, 10, 34, 1]


print(FindLargesstElement(arr))
print(FindSecondLargestElement(arr))
print(FindThirdLagestElement(arr))

