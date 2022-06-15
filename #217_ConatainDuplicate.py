"""
#Brute force
#Time Complexity: O(n^2) [It gets Time Limit Exceeded when n ≥10^5]
#Space Complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)): #range(i+1,soooo smart)
                if(nums[i] == nums[j]):
                    return True
        return False

#use sort()
#Time Complexity: O(n Log n)
#Space Complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  #!!!！
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
"""
#use set()
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_List = set()
        for i in range(len(nums)):
            if nums[i] in new_List:
                return True
            new_List.add(nums[i])
        return False
    
"""   
#use hash Table
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] not in hashTable:
                hashTable[nums[i]] = 1
            else:
                hashTable[nums[i]] += 1
        
        for i in range(len(nums)):
            if hashTable[nums[i]] >= 2:
                return True
        return False
""" 