class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            new_word = "".join(sorted(word))
            if new_word in anagrams:
                anagrams[new_word] += [word]
            else:
                anagrams[new_word] = [word]

        return [words for words in anagrams.values()]