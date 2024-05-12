class Solution:
    #Function to sort the array using bubble sort algorithm.
    def recursive_bubble_sort(self, arr, n):
        # Base case: If there's only one element, it's sorted.
        if n == 1:
            return
    
        # Make a single pass and bubble the largest element to the end
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
        # Largest element is fixed, recurse for the remaining array
        self.recursive_bubble_sort(arr, n - 1)


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.recursive_bubble_sort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends