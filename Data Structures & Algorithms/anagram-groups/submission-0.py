class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        characters = {}

        for word in strs:
            letters = ''.join(sorted(word))
            if letters not in characters:
                characters[letters] = []
            
            characters[letters].append(word)

        return [value for value in characters.values()]
            
