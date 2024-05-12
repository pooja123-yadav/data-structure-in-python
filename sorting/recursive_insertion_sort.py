class Solution:
    def recursive_insertion_sort(self,arr, n):
        # Base case: If there's only one element, it's already sorted.
        if n <= 1:
            return
        
        # Recursively sort the first n-1 elements
        self.recursive_insertion_sort(arr, n-1)
        
        # Insert the last element of the first n elements in its correct position
        last = arr[n-1]
        j = n-2
        
        # Move elements of arr[0..n-2] that are greater than last one position ahead
        while (j >= 0 and arr[j] > last):
            arr[j + 1] = arr[j]
            j = j - 1
        
        arr[j + 1] = last


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends