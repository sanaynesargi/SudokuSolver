
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def vaild(bo, num, pos):

    # num is the number that we have added to teh board
    # function to check if num is vaild when in inserted in position (pos)

    # we have already inserted the number, we are just making sure it is valid
    # pos is in the format that is returned out of find_empty() # row, col

    # Check row
    # loop through the row and check if the number is vaild in that row
    for i in range(len(bo[0])):

        # if we see the number in the row and it is not in the position we put it in, then return False
        # because there are two occurences of that number in the row which is illegal
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column (very similar to checking row)
    for i in range(len(bo)):
        # if we see the number in the column and it is not in the position we put it in, then return False
        # because there are two occurences of that number in the column which is illegal
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 grid that square is in (x = col, y = row)
    # get box by integer division
    # top-left is 0,0 in format box_x, box_y, as you go to the right and down it becomes
    # 0,1 0,2 1,0 1,1 1,2 2,0 2,1 2,2
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # loop from box origin, (box_y * 3, box_x * 3) to the square 3 spaces away, then do that 
    # the same amount of time to get all the squares in the 3x3 grid
    # we multiply them by 3 because box_x or box_y is going to be 0, 1, or 2, if we multiply
    # those by 3, we get the origin of that box

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            # loop through the box, check if any other element is the same as the one we inserted
            # then, check if it is in a different position then ours, if it is then there are two of
            # the same numbers in the box which is illegal, so we return False
            if bo[i][j] == num and (i, j) != pos:

                return False

    # if it passes all checks then return True
    return True

# function that implemets the backtacking algorithm to solve the sudoku board
def solve(bo):

    find = find_empty(bo) # find and empty square that we will use to try and solve the board
    # if find is None then we have completed teh board, because there is no 0 in the board
    # BASE CASE
    if find is None:

        return True
    else:
        # IMPLEMENTATION
        row, col = find # set the row and column of the empty square selected

    # try each number from 1 to 9 in the square, the first one we find that is valid
    # gets inserted
    # if we find that later there is no valid square then we backtrack until we find another valid square
    for i in range(1, 10):
        
        if vaild(bo, i, (row, col)):
            bo[row][col] = i # add the number to the board at the previously empty position

            # RECURSIVE CALL
            # call solve on the board again, if we can't then reset the position to 0
            if solve(bo):
                return True

            bo[row][col] = 0

# function to print board to terminal (utility)
def print_board(bo):

    for i in range(len(bo)):

        # print a horizontal line to seperate 3x3 chunks of board and each row of 3x3's in the board
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        # loop through each number on the board
        for j in range(len(bo[i])):

            # if we have printed 3 numbers (j % 3) and we have printed numbers because 0 % 3 is 0
            # then print a bar to seperate the 3 numbers from the next 3 numbers
            if j % 3 == 0 and j != 0:

                print(" | ", end="") # make sure there is no line added to the end of the string
                
            # if we are on the last element of the row then just print the last number and a line
            if j == len(bo[i]) - 1: 
                print(bo[i][j]) # we can move to next line 
            # if we still have more numbers to print, then print the number with a space after it to make
            # space for the next number
            else:
                print(str(bo[i][j]) + " ", end="") # stay on same line, don't print \n

def find_empty(bo):

    for i in range(len(bo)):

        for j in range(len(bo[i])):

            if bo[i][j] == 0:
                return (i, j) # row col

    return None


def main():
    print_board(board)
    print("\n\n\n")
    solve(board)
    print_board(board)

if __name__ == '__main__':
    main()