# https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1?page=1&category=Binary%20Search&difficulty=Medium&status=unsolved&sortBy=submissions

class Solution:

    def find(self,arr,n,k):
        s, e = 0, n-1
        first = self.first_occur(arr,s,e,k)
        last = self.last_occur(arr,s,e,k)

        return {"first": first, "last":last, "count":last-first+1} 


    def first_occur(sellf,arr,s,e,k):
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

    def last_occur(self,arr,s,e,k):
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
    
if __name__ == "__main__":
    obj = Solution()
    n=9
    x=5
    arr = [ 1, 3, 5, 5, 5, 5, 67, 123, 125]  
    res=obj.find(arr,n,x)
    print(res)