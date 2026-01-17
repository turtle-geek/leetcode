class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Time Complexity: O(n^2) for iterating through row and col of board
        # Space Complexity: O(n^2) for case of full sudoku board
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".":
                    continue
                
                index = (r//3)*3 + (c//3)

                if curr in rows[r] or curr in cols[c] or curr in boxes[index]:
                    return False
                
                rows[r].add(curr)
                cols[c].add(curr)
                boxes[index].add(curr)
        return True
