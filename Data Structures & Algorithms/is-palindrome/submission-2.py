class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        leftPointer = ''
        leftPointerIndex = 0
        rightPointer = ''
        rightPointerIndex = len(s) - 1

        for i in range(len(s) // 2):

            leftPointer = leftPointer + s[leftPointerIndex]
            rightPointer = rightPointer + s[rightPointerIndex]

            leftPointerIndex = leftPointerIndex + 1
            rightPointerIndex = rightPointerIndex - 1

        return leftPointer == rightPointer