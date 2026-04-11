class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in sortedMap:
                sortedMap[sortedS].append(s)
            else:
                sortedMap[sortedS] = [s]
        
        return list(sortedMap.values())
        