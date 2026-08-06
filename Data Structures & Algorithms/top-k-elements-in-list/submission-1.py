class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashNums = {}  # number -> frequency

        for i in nums:
            if i in hashNums:
                hashNums[i] += 1
            else:
                hashNums[i] = 1

        result = []

        for num, freq in sorted(hashNums.items(), key=lambda x: x[1], reverse=True):
            result.append(num)

            if len(result) == k:
                break

        return result