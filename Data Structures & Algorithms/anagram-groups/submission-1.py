class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == []:
            return [[""]]

        resHashMap = defaultdict(list)
        for letters in strs:
            count = [0] * 26

            for letter in letters:
                count[ord(letter) - ord("a")] += 1
            
            resHashMap[tuple(count)].append(letters)

        return list(resHashMap.values())




        
        # go through each letter
        # sort the letters then see if the previous sorted letter is equal
        # to the current sorted letter. If it's put it in that bucket. if 
        # not keep moving
        
