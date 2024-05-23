def search(arr, n, x):
    pivot_index = pivotIndex(arr,n)
    ans = -1, -1

    if pivot_index:

        if arr[pivot_index] <= x <= arr[n-1]:
            s,e = pivot_index, n-1
            # ans = searchkey(arr,s,e,k)
            first = first_occur(arr,s,e,x)
            last = last_occur(arr,s,e,x)
            ans = last - first + 1
        else:
            s,e = 0, pivot_index-1
            # ans = searchkey(arr,s,e,k)
            first = first_occur(arr,s,e,x)
            last = last_occur(arr,s,e,x)
            ans = last - first + 1

    else:
        s,e = 0, n-1
        # ans = searchkey(arr,s,e,k)
        first = first_occur(arr,s,e,x)
        last = last_occur(arr,s,e,x)
        ans = last - first + 1

    return ans



def pivotIndex(arr,n):
    low, high = 0 , n-1

    while low<high:
        mid = low + (high-low)//2

        if arr[mid] >= arr[high]:
            low = mid + 1
        else:
            high = mid

    return low

def searchkey(arr, s, e, k):

        while s<=e:
            mid = s+(e-s)//2

            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                s = mid + 1
            else:
                e = mid - 1

        return -1
        
def first_occur(arr,s,e,k):
        ans = -1
        while s<=e:
            mid = s+(e-s)//2
            if arr[mid]==k:
                ans = mid
                e = mid - 1
            elif arr[mid]>k:
                e = mid - 1
            else:
                s = mid +1

        return ans

def last_occur(arr,s,e,k):
    ans = -1
    while s<=e:
        mid = s+(e-s)//2
        if arr[mid]==k:
            ans = mid 
            s = mid + 1
        elif arr[mid]> k:
            e = mid - 1
        else:
            s = mid +1
    return ans

    

arr = [12, 15, 15,15,15,18, 2, 4]
print(search(arr,len(arr), 15))
