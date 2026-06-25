class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return []
        
        hashmap = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            hashmap[key].append(s)
        
        return list(hashmap.values())

        