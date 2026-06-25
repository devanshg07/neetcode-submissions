class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNumbers = {}

        for i in range(len(nums)):
            subtract = target - nums[i]

            if subtract in seenNumbers:
                return [seenNumbers[subtract], i]

            seenNumbers[nums[i]] = i
