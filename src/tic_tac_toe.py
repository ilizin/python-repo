import random
import time

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
moves = []

def draw_board(board, only_printable):
    print()
    for row in board:
        for cell in row:
            if (only_printable or cell == 'X' or cell == 'O'):
                print("|", cell, sep="", end="") 
            else:
                print("|", " ", sep="", end="") 
        print("|")
 
def computer_move(moves):
    print("\nThe computer move is: ", end="")
    time.sleep(2)
    move = random.randint(1, 9)
    while (move in moves):
        move = random.randint(1, 9)
    moves.append(move)
    print(move)
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

def player_move(move):
    while(True):
        try:
            move = int(input("\nEnter your next move: "))
            if (move in moves):
                print("\nYour move is taken, please try again")
            elif (move < 1 or move > 9):
                print("\nYour move is wrong, please input a value from 1 to 9")
            else:   
                moves.append(move)
                return move
        except ValueError:
            print("\nYour move is wrong, please input a value from 1 to 9")  
            
print("\nReady for Tic Tac Toe? Let's play!")
print("\nThe player : X")
print("The computer : O")
draw_board(board, True)
while(True):
    move = player_move(moves)
    board[(move - 1) // 3][(move % 3) - 1] = 'X'
    draw_board(board, False)
    if check_win(board):
        print("\nYou win!")
        break
    move = computer_move(moves)
    board[(move - 1) // 3][(move % 3) - 1] = 'O'
    draw_board(board, False)
    if check_win(board):
        print("\nComputer win!")
        break

    
    
    