class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = dict()
        tCount = dict()

        for ch in s:
            if ch in sCount:
                sCount[ch] += 1
            else:
                sCount[ch] = 1
        
        for ch in t:
            if ch in tCount:
                tCount[ch] += 1
            else:
                tCount[ch] = 1

        return sCount == tCount