from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for row in board:
            hashmap = defaultdict(int)
            
            for s in row:
                if s != ".":
                    if s in hashmap:
                        return False
                    else:
                        hashmap[s] = 1
                
        for col in range(n):
            hashmap = defaultdict(int)

            for row in range(n):
                s = board[row][col]
                if s != ".":
                    if s in hashmap:
                        return False
                    else:
                        hashmap[s] = 1
        
        subGrids = [[] for _ in range(n)]
        for row in range(n):
            for col in range(n):
                value = board[row][col]

                if value != ".":
                    subGridIndex = (row // 3)*3 + (col // 3)
                    subGrids[subGridIndex].append(value)

        for subGrid in subGrids:
            hashmap = defaultdict(int)
            for s in subGrid:
                if s in hashmap:
                    return False
                else:
                    hashmap[s] = 1
        
        return True