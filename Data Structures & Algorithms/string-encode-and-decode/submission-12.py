class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for word in strs:
            encoding += f"{len(word)}#{word}"

        return encoding

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            print(i)
            j = i
            while s[j] != '#':
                j += 1

            print(s[i:j])

            length = int(s[i:j])
            word = s[i + (j - i) + 1 : i + (j - i) + length + 1]
            print(word)
            result.append(word)
            i = i + (j - i) + length + 1

        return result
