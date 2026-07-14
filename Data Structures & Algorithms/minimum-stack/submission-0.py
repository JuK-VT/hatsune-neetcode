class MinStack:

    def __init__(self):
        self._stack = []
        self._sorted = []

    def push(self, val: int) -> None:
        if not self._sorted:
            self._sorted.append(val)
        else:
            self._sorted.append(min([val, self._sorted[-1]]))
        self._stack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._sorted.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._sorted[-1]
        
