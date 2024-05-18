def Leader(arr):
    n = len(arr)
    leader = [arr[-1]]

    for i in range(n-2,-1,-1):
        if arr[i] >= leader[0]:
            leader.insert(0,arr[i])

    return leader

arr =  [16, 17, 4, 3, 5, 2]
print(Leader(arr))