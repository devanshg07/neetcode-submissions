class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashSetS = {}
        hashSetT = {}

        if(len(s) != len(t)):
            return False

        for i in range(len(s)):
            hashSetS[s[i]] = hashSetS.get(s[i], 0 ) + 1
            hashSetT[t[i]] = hashSetT.get(t[i], 0 ) + 1
        
        
        if hashSetS == hashSetT:
            return True
        else:
            return False
            

        

        