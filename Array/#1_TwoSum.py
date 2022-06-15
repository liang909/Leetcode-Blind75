#O(N^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            rem  = target - nums[i]
            for j in range(i+1,n):
                if rem == nums[j]:
                    return [i,j]

#O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dir = {}
        for i in range(len(nums)):
            rem = target - nums[i] 
            if rem in dir:                    
                return [dir[rem],i]     
            else:
                dir[nums[i]] = i    
