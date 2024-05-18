def sort012(arr):
    count0, count1, count2 = 0, 0, 0

    for num in arr:
        if num == 0:
            count0 += 1

        elif num == 1:
            count1 += 1

        elif num == 2:
            count2 += 1

    i = len(arr)-1

    while count2 > 0:
        arr[i] = 2
        count2 -= 1
        i -= 1

    while count1 > 0:
        arr[i] = 1
        count1 -= 1
        i -= 1

    while count0 > 0:
        arr[i] = 0
        count0 -= 1
        i -= 1

    return arr

arr = [0, 2, 1, 2, 0]
print(sort012(arr))