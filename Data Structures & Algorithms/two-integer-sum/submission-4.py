class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevElements = {} #contains past values and index in array

        for i, n in enumerate(nums):
            diffNum = target - n
            if diffNum in prevElements:
                return[prevElements[diffNum], i]
            prevElements[n] = i
        return