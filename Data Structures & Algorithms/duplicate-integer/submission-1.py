class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNumbers = set()

        for num in nums:
            if(num in seenNumbers):
                return True
            else:
                seenNumbers.add(num)

        return False
