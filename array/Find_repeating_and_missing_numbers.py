def FindRepeatingAndMissing(arr):
    n = len(arr)
    seen = {}
    repeating = -1
    missing = -1

    for num in arr:
        seen[num] = seen.get(num,0) + 1

    for num in range(1,n+1):
        if num not in seen:
            missing = num
        else:
            if seen[num] > 1:
                repeating = num
        if repeating != -1 and missing != -1:
            break

    return repeating, missing

arr = [1,2,3,3,5,6]
print(FindRepeatingAndMissing(arr))

