class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            midIndex = left + (right - left) // 2

            if nums[midIndex] == target:
                return midIndex
            
            elif nums[midIndex] > target:
                right = midIndex - 1
                    
            else:
                left = midIndex + 1

        return -1