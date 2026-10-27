class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_letters = defaultdict(list)

        for word in strs:
            res = [0] * 26
            for wrd in word:
                key = ord(wrd) - ord('a')
                res[key] += 1
            key = tuple(res)
            if key in map_letters:
                map_letters[key].append(word)
            
            else:
                map_letters[key] = [word]

        return list(map_letters.values())
            