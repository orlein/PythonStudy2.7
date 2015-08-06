'''
Created on 2015. 8. 5.

@author: PCJ
'''


if __name__ == '__main__':
    pass
from random import randint



def makeboard(board, board_row, board_col):
    for row in range(board_row):
        board.append([])     
        for col in range(board_col):  # @UnusedVariable
            board[row].append("O")
    return

def set_ship(board):
    ship_row = randint(0, len(board)-1)
    ship_col = randint(0, len(board[0])-1)
    return ship_row, ship_col
def set_ships(board, num_ships):
    ships = []
    for num in range(num_ships):  # @UnusedVariable
        (row, col) = set_ship(board)
        if(check_duplication(ships, (row, col)) == False):
            ships.append((row, col))
    return ships
def check_duplication(lst, i):
    for elem in range(len(lst)):
        if (lst[elem] == i):
            return True 
    return False

def print_board(board):    
    for row in board:
        print(" ".join(row))
    return 
def check_2d((x1,y1),(x2,y2)):
    result = abs(x1-x2) + abs(y1-y2)
    return result
def firingcheck(ships,(x,y)):
    check = []
    for i in range(len(ships)):
        check.append(check_2d(ships[i],(x,y)))
    return min(check)
def fire(board, ships, attempts):
    result = False
    count = attempts
    check = 0
    num_of_ships = len(ships)
    while((result == False) and (count > 0)):
        print("attempts remaining:%d"%(count))
        guess_row = int(raw_input("Guess Row:")) - 1
        guess_col = int(raw_input("Guess Col:")) - 1
        check = firingcheck(ships,(guess_row, guess_col))
        if (check == 0):
            print("A ship sunk!")
            board[guess_row][guess_col] = "S"
            num_of_ships = num_of_ships - 1
            print_board(board)
            if(num_of_ships == 0):
                result = True
            else:
                result = False
        elif(guess_row <0 or guess_row>len(board)) or (guess_col<0 or guess_col > len(board[guess_row])):
            print("Hey, it's out of battle boundary!")
            result = False
        elif(check > 0):
            if(check == 1):
                print("Closed!")
                board[guess_row][guess_col] = "C"
            elif(check == 2):
                print("A ship is near the drop site!")
                board[guess_row][guess_col] = "N"
            else:
                print("A ship is far away! try again.")
                board[guess_row][guess_col] = "X"
            print_board(board)
            result = False
        count = count - 1
    print("End firing, Ships remaining:%d"%(num_of_ships))
    return result

def fire_a_ship(board, (ship_row, ship_col), attempts):  
    result = False
    count = attempts
    check = 0
    while((result == False) and (count > 0)):
        print("attempts remaining:%d"%(count))
        guess_row = int(raw_input("Guess Row:")) - 1
        guess_col = int(raw_input("Guess Col:")) - 1
        check = check_2d(ship_row,ship_col,guess_row,guess_col)
        if (check == 0):
            print("A ship sunk!")
            board[guess_row][guess_col] = "S"
            print_board(board)
            result = True
        elif(guess_row <0 or guess_row>len(board)) or (guess_col<0 or guess_col > len(board[guess_row])):
            print("Hey, it's out of battle boundary!")
            result = False
        elif(check > 0):
            if(check == 1):
                print("Closed!")
                board[guess_row][guess_col] = "C"
            elif(check == 2):
                print("A ship is near the drop site!")
                board[guess_row][guess_col] = "N"
            else:
                print("A ship is far away! try again.")
                board[guess_row][guess_col] = "X"
            print_board(board)
            result = False
        count = count - 1
    print("End firing")
    return result

def start_game_msg(stage):
    print("Stage %d Start"%(stage))
    return

def cheat_A(ship_row, ship_col):
    print("CHEATING...:%d, %d"%(ship_row+1, ship_col+1))
    
def cheat_B(ships):  # @DuplicatedSignature
    print("CHEATING...")
    print(ships)
    return

def game(stages):
    stage = 1
    print("OVERALL STAGES: %d"%(stages))
    while(stage <= stages):
        board = []
        attempts = 10
        makeboard(board, 5, 10)
        print_board(board)
        ship_row, ship_col = set_ship(board)
        cheat_A(ship_row, ship_col)
        start_game_msg(stage)
        fire_a_ship(board, ship_row, ship_col, attempts)
        stage = stage + 1
    print("END GAME")
    return

def demo(stages):    
    stage = 1
    print("OVERALL STAGES: %d"%(stages))
    while(stage <= stages):
        board = []
        ships = []
        row = 5
        col = 10
        attempts = row * col
        makeboard(board, row, col)
        print_board(board)
        ships = set_ships(board, int(attempts / 10))
        '''cheat_B(ships)'''
        start_game_msg(stage)
        fire(board, ships, attempts)
        stage = stage + 1
    print("END GAME")
    return

demo(1)
