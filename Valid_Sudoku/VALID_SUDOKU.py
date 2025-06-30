import re

class Solution:
    rowCheck:list[list[str]]
    columnCheck:list[list[str]] 
    squareCheck:list[list[str]] 
    
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        isValid:bool = True
        self.rowCheck= [[] for i in range(len(board))]
        self.columnCheck = [[] for i in range(len(board))]
        self.squareCheck = [[] for i in range(len(board))]
        
        for i, row in enumerate(board):
            square_row = i//3 * 3
            
            for j, num in enumerate(row):
                square_column = j//3
                
                if num == ".":
                    continue
                elif re.match(r"\D", num):
                    isValid = False
                
                if num in self.columnCheck[j] or num in self.rowCheck[i] or num in self.squareCheck[square_row + square_column]:
                    isValid = False
                    return isValid
                
                self.columnCheck[j].append(num)
                self.rowCheck[i].append(num)
                self.squareCheck[square_row + square_column].append(num)
        
        return isValid
    
    
if __name__ == "__main__":
    mySolution = Solution()
    isValid = mySolution.isValidSudoku([["1","2",".",".","3",".",".","6","."],
                                        ["4",".",".","5",".",".",".",".","."],
                                        [".","9","8",".",".",".","8",".","3"],
                                        ["5",".",".",".","6",".",".",".","4"],
                                        [".",".",".","8",".","3",".",".","5"],
                                        ["7",".",".",".","2",".",".",".","6"],
                                        [".",".",".",".",".",".","2",".","."],
                                        [".",".",".","4","1","9",".",".","8"],
                                        [".",".",".",".","8",".",".","7","9"]])
    # isValid = mySolution.isValidSudoku([["7",".",".",".","4",".",".",".","."],
    #                                     [".",".",".","8","6","5",".",".","."],
    #                                     [".","1",".","2",".",".",".",".","."],
    #                                     [".",".",".",".",".","9",".",".","."],
    #                                     [".",".",".",".","5",".","5",".","."],
    #                                     [".",".",".",".",".",".",".",".","."],
    #                                     [".",".",".",".",".",".","2",".","."],
    #                                     [".",".",".",".",".",".",".",".","."],
    #                                     [".",".",".",".",".",".",".",".","."]])

    print(f"Mi solución es válida?: {isValid}")    