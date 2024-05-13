class Solution(object):

    def peakIndexInMountainArray(self, arr, n):
        s,e = 0, n-1

        while s<e:
            mid = s+(e-s)//2

            if arr[mid] < arr[mid+1]:
                s = mid + 1
            else:
                e = mid

        return s

if __name__ == "__main__":
    obj = Solution()
    n=4
    arr = [0,10,5,2]
    res=obj.peakIndexInMountainArray(arr,n)
    print(res)