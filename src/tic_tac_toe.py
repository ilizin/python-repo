import random

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
moves = []

def draw_board(board):
    for row in board:
        print("|", row[0], "|", row[1], "|", row[2], "|", sep="")
 
def computer_move(moves):
    move = random.randint(1, 9)
    while (move in moves):
        move = random.randint(1, 9)
    return move
    
def check_win(board):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2]):
        return True
    if (board[1][0] == board[1][1] and board[1][0] == board[1][2]):
        return True
    if (board[2][0] == board[2][1] and board[2][0] == board[2][2]):
        return True    
    if (board[0][0] == board[1][0] and board[0][0] == board[2][0]):
        return True
    if (board[0][1] == board[1][1] and board[0][1] == board[2][1]):
        return True
    if (board[0][2] == board[1][2] and board[0][2] == board[2][2]):
        return True 
    if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return True  
    if (board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        return True  
        
print()
while(True):
    try:
        move = int(input("Enter your next move: "))
        moves.insert(0, move)
        print()
        board[(move - 1) // 3][(move % 3) - 1] = 'X'
        draw_board(board)
        if check_win(board):
            print("\nYou win!")
            break
        print()
        move = computer_move(moves)
        moves.insert(0, move)
        print("The computer move is: ", move)
        print()
        board[(move - 1) // 3][(move % 3) - 1] = 'O'
        draw_board(board)
        if check_win(board):
            print("\nComputer win!")
            break
        print()
    except ValueError:
            print("The move is worong, please input a value from 1 to 9")
    
    
    