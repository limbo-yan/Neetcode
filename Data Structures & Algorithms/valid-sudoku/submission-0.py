class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        groups = {}
        colSet = {}
        for i in range(9):
            rowSet = set()
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rowSet:
                    return False
                rowSet.add(num)

                if j in colSet:
                    if num in colSet[j]:
                        return False
                    colSet[j].add(num)
                else:
                    colSet[j] = set([num])
                
                group = (i // 3) + (j // 3) * 3
                if group in groups:
                    if num in groups[group]:
                        return False
                    groups[group].add(num)
                else:
                    groups[group] = set([num])

        
        return True

                

        