class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_letters = defaultdict(list)

        for word in strs:
            res = [0] * 26
            for wrd in word:
                key = ord(wrd) - ord('a')
                res[key] += 1
            tuple_key = tuple(res)
            if tuple_key in map_letters:
                map_letters[tuple_key].append(word)
            
            else:
                map_letters[tuple(res)] = [word]

        return list(map_letters.values())
            