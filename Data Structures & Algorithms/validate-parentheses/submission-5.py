class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        char_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in char_map:
                if st and st[-1] == char_map[char]:
                    st.pop()
                else:
                    return False
            else:
                st.append(char)
        
        return True if not st else False
