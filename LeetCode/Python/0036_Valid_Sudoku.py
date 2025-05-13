# LeetCode
# Problem 36: Valid Sudoku
# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Create list with 9 lists for 9 boxes
        list_box = [[] for _ in range(9)]

        for row in range(9):
            list_col = []
            list_row = []
            for col in range(9):
                #Traverse each col, row by row              
                if board[col][row].isdigit():
                    #print(board[col][row])

                    #Validate each col
                    if board[col][row] in list_col:
                        #print(f"duuplicate found: {board[col][row]}")
                        return False
                    list_col.append(board[col][row]) 

                #Traverse each list/row col by col
                if board[row][col].isdigit():
                    #print(f"number:{board[row][col]} in col:{col} row:{row}")

                    #Validate each row
                    if board[row][col] in list_row:
                        #print(f"duplicate found: {board[row][col]}")
                        return False
                    list_row.append(board[row][col])

                    #build list for each box numbered left to right                                
                    if  row < 3 and col < 3:
                        #print("box one")
                        list_box[0].append(board[row][col])
                    elif row < 3 and col < 6 and col > 2:
                        #print("box two")
                        list_box[1].append(board[row][col])
                    elif row < 3 and col > 5:
                        #print("box three")
                        list_box[2].append(board[row][col])
                    elif row < 6 and row > 2 and col < 3:
                        #print("box four")
                        list_box[3].append(board[row][col])
                    elif row < 6 and row > 2 and col > 2 and col < 6:
                        #print("box five")
                        list_box[4].append(board[row][col])
                    elif row < 6 and row > 2 and col > 5:
                        #print("box six")
                        list_box[5].append(board[row][col])
                    elif row > 5 and col < 3:
                        #print("box seven")
                        list_box[6].append(board[row][col])
                    elif row > 5 and col > 2 and col < 6:
                        #print("box eight")
                        list_box[7].append(board[row][col])
                    elif row > 5 and col > 5:
                        #print("box nine")
                        list_box[8].append(board[row][col])

        #Validate each box for duplicates
        #print(list_box)
        for box in list_box:
            for num in box:
                if box.count(num) > 1:
                    #print(f"found duuupe in {box}")
                    return False

        return True
