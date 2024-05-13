class Solution(object):
    def pivotIndex(self, nums, n):
        
        # forming a running sum array
        for i in range(1, n):
            nums[i] += nums[i-1]

        # side case when the pivot is the first element
        if nums[0] == nums[-1]:
            return 0
        
        # checking for a pivot
        for i in range(1, n):
            if nums[-1] - nums[i] == nums[i-1]:
                return i
        # did not find a pivot
        return -1


if __name__ == "__main__":
    obj = Solution()
    n=6
    arr = [1,7,3,6,5,6]
    res=obj.pivotIndex(arr,n)
    print(res)