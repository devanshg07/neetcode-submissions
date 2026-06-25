class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums 
            
        hashmap = defaultdict(int)
        
        for num in nums:
            hashmap[num] += 1

        sortedNums = sorted(hashmap, key = hashmap.get, reverse = True)
        return sortedNums[:k] 

            