def sub(nums, t):
    seen = dict()
    result = set()

    for k, num in enumerate(nums):
        c = t-num
        if c in seen:
            result.add((c,num))
        else:
            seen[num] = k

    return result

a = [10, 20, 30, 40, 10]
t = 50
print(sub(a, t))
