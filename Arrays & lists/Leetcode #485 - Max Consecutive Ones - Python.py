class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans = 0
        currentCount = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                currentCount = 0
            else:
                currentCount += 1
            
            if currentCount > ans:
                ans = currentCount

        return ans
