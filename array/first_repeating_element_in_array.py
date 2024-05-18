def FirstRepeatingElement(arr):
    seen = {}
    ans = float("inf")

    for k,v in enumerate(arr):
        if v in seen:
            ans = min(ans, seen[v])
        else:
            seen[v] = k

    return ans

arr = [1, 5, 3, 4, 5, 3, 5, 6]
print(FirstRepeatingElement(arr))

