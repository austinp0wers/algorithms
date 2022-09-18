# First solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(arr,target):
            left = 0
            right = len(arr)-1
            while left <= right:
                middle = (left + right) // 2
                if arr[middle] < target: 
                    left = middle +1
                else: 
                    right = middle - 1
            return left
        
        def findRight(arr,target):
            left = 0
            right = len(arr) -1
            res = 0
            while left <= right:
                middle = (left+right) //2
                if arr[middle] > target: 
                    right = middle - 1
                else: 
                    left = middle + 1
            return right
        
        a = findLeft(nums,target)
        b = findRight(nums, target)
        if a == len(nums) or nums[a] != target: return [-1,-1]
        return [a,b]

# Smarter solution, that surprized me
# instead of finding left, right in 2 different functions
# find index of target+1 than -1 from there
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(arr,target):
            left = 0
            right = len(arr)-1
            while left <= right:
                middle = (left + right) // 2
                if arr[middle] < target: 
                    left = middle +1
                else: 
                    right = middle - 1
            return left
        
        a = findLeft(nums,target)

        if a == len(nums) or nums[a] != target: return [-1,-1]
        return [a, findLeft(nums, target+1)-1]