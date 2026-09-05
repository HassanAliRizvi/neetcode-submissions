class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            if tuple(freq) in groups:
                groups[tuple(freq)].append(word)
            else:
                groups[tuple(freq)] = [word]
        
        return list(groups.values())

        # space = O(m)
        # time = O(n) * O(m log m)
            


        