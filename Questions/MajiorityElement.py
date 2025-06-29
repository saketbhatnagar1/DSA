nums = [3,2,3,4,4,4,4,4,4,5,5,5,6,5,5,5,5,5,5,6]
majiority = len(nums)//2
print(majiority)
print(sorted(nums))
print(sorted(nums)[majiority])

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = int((len(nums)/2))
        maxfreq = 0
        for i in nums:
            count[i] = count.get(i,0)+1
            if count[i]>n:
                return i
            
        
        