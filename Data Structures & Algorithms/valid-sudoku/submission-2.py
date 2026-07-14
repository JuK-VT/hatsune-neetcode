class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [''.join(row).replace('.', '') for row in board]
        
        cols = [[] for i in range(9)]

        squares = [[] for i in range(9)]

        steps = 0
        square = 0

        for i, row in enumerate(board):
            squares[square].extend(row[:3])
            squares[square + 1].extend(row[3:6])
            squares[square + 2].extend(row[6:])
            steps += 1
            for j, element in enumerate(row):
                cols[j].append(element)

            if steps == 3:
                square += 3
                steps = 0

        cols = [''.join(col).replace('.', '') for col in cols]
        squares = [''.join(col).replace('.', '') for col in squares]

        for series in rows + cols + squares:
            if len(series) != len(set(series)):
                return False
        
        return True
