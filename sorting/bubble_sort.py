class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n):
            swap = False
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    swap = True
            if swap == False:
                return arr

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends