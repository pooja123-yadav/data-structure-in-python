def ProductExceptItself(arr):
    n = len(arr)
    result = [1] * n

    leftProduct = 1
    for i in range(n):
        result[i] = result[i] * leftProduct
        leftProduct *= arr[i]

    righProduct = 1
    for i in range(n-1,-1,-1):
        result[i] = result[i] * righProduct
        righProduct *= arr[i]

    return result

arr = [10, 3, 5, 6, 2]
print(ProductExceptItself(arr))
