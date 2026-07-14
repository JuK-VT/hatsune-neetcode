class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        res = []

        def backtrack(open_p, close_p):
            if open_p == close_p == n:
                res.append("".join(s))
                return

            if open_p < n:
                s.append("(")
                backtrack(open_p + 1, close_p)
                s.pop()

            if close_p < open_p:
                s.append(")")
                backtrack(open_p, close_p + 1)
                s.pop()

        backtrack(0, 0)
        return res
