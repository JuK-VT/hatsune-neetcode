from operator import add, truediv, mul, sub

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op_map = {"*": mul, "/": truediv, "+": add, "-": sub}

        for token in tokens:
            if token in "*/+-":
                new_number = op_map[token](s[-2], s[-1])
                s.pop()
                s.pop()
                s.append(int(new_number))
            else:
                s.append(int(token))

        return s.pop()
