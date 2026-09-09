from sympy import prime

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = dict()

        for word in strs:
            index = 1
            for ch in word:
                index *= prime(ord(ch))
            if index in anagramGroups:
                anagramGroups[index].append(word)
            else:
                anagramGroups[index] = [word]
        
        return list(anagramGroups.values())