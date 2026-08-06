from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        resultHash = defaultdict(list) # charcount -> list of words

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            resultHash[tuple(count)].append(s)

        return list(resultHash.values())