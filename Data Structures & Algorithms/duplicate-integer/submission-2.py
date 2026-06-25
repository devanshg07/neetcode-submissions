class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNumbers = set()

        for i in range(len(nums)):
            if(nums[i] in seenNumbers):
                return True
            else:
                seenNumbers.add(nums[i])

        return False
