import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def Board():
    print("\n")
    print(f"{the_board['7']}|{the_board['8']}|{the_board['9']}  7|8|9")
    print("-+-+-")
    print(f"{the_board['4']}|{the_board['5']}|{the_board['6']}  4|5|6")
    print("-+-+-")
    print(f"{the_board['1']}|{the_board['2']}|{the_board['3']}  1|2|3")
    print("\n")


the_board = { '7' : " ", '8' : " ", '9' : " ", 
              '4' : " ", '5' : " ", '6' : " ", 
              '1' : " ", '2' : " ", '3' : " ", }

def game():
    count = 0
    turn = 'X'

    for i in range(10):
        Board()
        # print()
        move = input(f"It's your turn {turn} Choose your move: ")

        if the_board[move] == " ":
            the_board[move] = turn
        else:
            print("That place is already filled.\nMove to which place?")
            move = input()
            if the_board[move] == " ":
                the_board[move] = turn

        count += 1

        if count >= 5:
            if the_board['1'] == the_board['2'] == the_board['3'] != " " :
                Board()
                print("\n***Game Over***\n")
                print(f"{turn} you have  won")
                break
            elif  the_board['4'] == the_board['5'] ==  the_board['6'] != " ":
                Board()
                print("\n***Game Over***\n")
                print(f"{turn} you have  won")
                break
            elif the_board['7'] == the_board['8'] == the_board['9'] != " ":
                Board()
                print("\n***Game Over***\n")
                print(f"{turn} you have  won")
                break

            elif the_board['1'] == the_board['4'] == the_board['7'] != " ":
                Board()
                print("\n***Game Over***\n")
                print(f"{turn} you have  won")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != " ":
                Board()
                print("\n***Game Over***\n")
                print(f"{turn} you have  won")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != " ":
                Board()
                print("\n***Game Over***\n")
                print(f"{turn} you have  won")
                break

            elif the_board['1'] == the_board['5'] == the_board['9'] != " ":
                Board()
                print("\n***Game Over***\n")
                print(f"{turn} you have  won")
                break
            elif the_board['3'] == the_board['5'] == the_board['7'] != " ":
                Board()
                print("\n***Game Over***\n")
                print(f"{turn} you have  won")
                break
        
        if count == 9:
            print("\n***Game Over***\n")
            print("It's a tie")
        
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

game()


print("\n")
restart = input("Do u want to restart the game(Y/N): ").lower()
clearConsole()
if restart == "y":
    for keys in the_board.keys():
        the_board[keys] = " "
    
    game()