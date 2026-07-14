class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in '({[':
                print('append')
                st.append(char)
            else:
                if len(st) == 0:
                    return False
                second = st.pop()
                if char == ')' and second != '(':
                    return False
                if char == '}' and second != '{':
                    return False
                if char == ']' and second != '[':
                    return False
        
        return True if len(st) == 0 else False
