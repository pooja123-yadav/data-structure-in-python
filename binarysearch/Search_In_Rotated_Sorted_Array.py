class Solution:

    def search(self,arr,n,k):
        s,e = 0, n-1
        pivotIndex = self.pivotIndex(arr,n)
        
        ans = -1
        if pivotIndex:
            if arr[pivotIndex] <= k <= arr[n-1]:
                s,e = pivotIndex, n-1
                ans = self.searchkey(arr,s,e,k)
            else:
                s,e = 0, pivotIndex-1
                ans = self.searchkey(arr,s,e,k)
        else:
            s , e = 0, n-1
            ans = self.searchkey(arr, s, e, k)

        return ans

    def pivotIndex(self,arr,n):
        s, e = 0 , n-1
        while s<e:
            mid = s+(e-s)//2
            if arr[mid]>=arr[e]:
                s = mid + 1
            else:
                e = mid

        return s
    
    def searchkey(self, arr, s, e, k):

        while s<=e:
            mid = s+(e-s)//2

            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                s = mid + 1
            else:
                e = mid - 1

        return -1

if __name__ == "__main__":
    arr = [8, 9, 4, 5]
    n = 4
    k = 5
    obj = Solution()
    res = obj.search(arr,n,k)
    print(res)