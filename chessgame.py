def chessboard():
    chessBoard = [[" ","H","G","F","E","D","C","B","A"],
                  ["1","r","n","b","q","k","b","n","r"],
                  ["2","p","p","p","p","p","p","p","p"],
                  ["3",".",".",".",".",".",".",".","."],
                  ["4",".",".",".",".",".",".",".","."],
                  ["5",".",".",".",".",".",".",".","."],
                  ["6",".",".",".",".",".",".",".","."],
                  ["7","P","P","P","P","P","P","P","P"],
                  ["8","R","N","B","Q","K","B","N","R"]]
    for i in range(9):
        for t in range(9):
            print(chessBoard[i][t], end=" ")
        print()
    return chessBoard

def userInput():
    userInput = input("make your move, i.e H2 H3\n")
    return userInput

def validNotation():
    while True:
        chessMove = userInput()
        if len(chessMove) != 5:
            print("that is not valid notation. Try again.1")
            continue
        move = chessMove.split()
        row1 = move[0][0].lower()
        column1 = move[0][1]
        row2 = move[1][0].lower()
        column2 = move[1][1]
       
        if (row1 == 'h' or row1 == 'g' or row1 == 'f' or row1 == 'e' or row1 == 'd' or row1 == 'c' or row1 == 'b' or row1 == 'a') and \
           (row2 == 'h' or row2 == 'g' or row2 == 'f' or row2 == 'e' or row2 == 'd' or row2 == 'c' or row2 == 'b' or row2 == 'a') and \
           (column1 == '1' or column1 == '2' or column1 == '3' or column1 == '4' or column1 == '5' or column1 == '6' or column1 == '7' or column1 == '8') and \
           (column2 == '1' or column2 == '2' or column2 == '3' or column2 == '4' or column2 == '5' or column2 == '6' or column2 == '7' or column2 == '8'):
            return False
        else:
            print("that is not valid notation2. Try again.2")
            continue

def playGame():
        chessboard()
        validNotation()
        
playGame()