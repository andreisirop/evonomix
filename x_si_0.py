import random
while True:
    board = [" "for i in range(9)]


    def print_board():
        row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
        row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
        row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9|")
    print("")
    print("Ti-am lasat tabla cu numerele corespunzatoare fiecarui patratel!")

    def player_move(icon):
        if icon == "X":
            number = 1
        elif icon == "O":
            number = 2
        print("Este randul jucatorului {}!".format(icon))
        choice = int(input("Introdu mutarea ta(1-9): ").strip())
        
        if board[choice-1] == " ":
            board[choice-1] = icon
            board[choice-1] == " "
            
        
            

        elif board[choice-1] == "X" or board[choice-1] == "O":
            print()
            print("Acest spatiu este ocupat deja!")
            player_move(icon)
            
            
            
            
       

    def is_victory(icon):
        if (board[0] == icon and board[1] == icon and board[2] == icon)or\
           (board[3] == icon and board[4] == icon and board[5] == icon)or\
           (board[6] == icon and board[7] == icon and board[8] == icon)or\
           (board[0] == icon and board[3] == icon and board[6] == icon)or\
           (board[1] == icon and board[4] == icon and board[7] == icon)or\
           (board[2] == icon and board[5] == icon and board[8] == icon)or\
           (board[2] == icon and board[4] == icon and board[6] == icon)or\
           (board[0] == icon and board[4] == icon and board[8] == icon):
            return True
        else:
            return False

    def is_draw():
        if " " not in board:
            return True
        else:
            return False
            
        


    while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            print("Jucatorul cu X a castigat! Felicitari!!")
            break
        elif is_draw():
            print("Este egalitate!!")
            break
        player_move("O")
        if is_victory("O"):
            print_board()
            print("Jucatorul cu O a castigat! Felicitari!!")
            break
        elif is_draw():
            print("Este egalitate!!")
            break
    joaca_din_nou_alegeri = ("da","nu")
    joaca_din_nou = input("Doresti sa joci din nou ? (Da sau nu): ").strip().lower()
    while joaca_din_nou not in joaca_din_nou_alegeri:
        joaca_din_nou = input("Doresti sa joci din nou ? (Da sau nu): ").strip().lower()
    if joaca_din_nou == "da":
        joaca_din_nou = True
    else:
        break

    # 73 linii de cod scris
    

    


