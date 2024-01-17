from functions import * #importation des fonctions pour pouvoir jouer au jeu

def player_vs_computer(end_game: int,board_game: list)->None:
    '''
    This function allows you to play the game against a computer
    :param end_game: int
    :param board_game: list
    :return: None
    '''
    print('The computer generate a code')
    board = copy_boar_model(board_game) #copie du tableau
    code = generate_code(color) #génération du code
    count_ligne = 1
    end = 0
    print("You must find the code that is composed of 4 colors.")   #affichage des règles
    print("Possible colors are Red, Green, Blue and Yellow.")
    print("On both sides of the board are randomly orders indicators :")
    print("- G for Good colors \n- M for Misplaced colors \n")
    display_bord(board)
    code_player = input('Enter your code : ') #demande au player de entrer un code
    while True:    #tant que c'est vrai on excute la boucle
        for i in range(30): #nettoyer la console
            print('\n')
        if valid_code(code_player, color):  # si le code est valide on entre dans la condition
            print("You must find the code that is composed of 4 colors.") #affichage des règles
            print("Possible colors are Red, Green, Blue and Yellow.")
            print("On both sides of the board are randomly orders indicators :")
            print("- G for Good colors \n- M for Misplaced colors \n")
            indicators = verify_code(code_player, code)  #obtention des indicateurs de jeux
            place_in_board(board, code_player, count_ligne)  #place le code du joueur dans le tableau
            place_in_board_indicators(board, code_player, code, count_ligne, indicators) #place le code du joueur dans le tableau
            display_bord(board)
            if code_player == ''.join(code): # si le code du joueur est le même que le code de l'ordinateur le joueur gagne
                print("You win")
                break #fin de la boucle
            count_ligne += 1
            end += 1
            if end == end_game: #cas pour la derniere ligne du plateau
                if ''.join(code) == code_player: #si le joueur gagne
                    print("You win")
                    break #fin de la boucle
                else: #cas ou le joueur perd
                    print(f'You lost... The code were {''.join(code)}')
                    break #fin de la boucle
            code_player = input('Enter your code : ') #demande au joueur un code
        else:
            code_player = input('Invalid input. Enter your code : ') #cas ou le code n'est pas valide



def player_vs_player(end_game: int, board_game: list)->None:
    '''
    This function allows you to play the game against a player
    :param end_game: int
    :param board_game: list
    :return: None
    '''
    board = copy_boar_model(board_game) #copie du tableau
    code = list(input("The player enters a code to guess (R/G/B/Y) : ")) #code que le joueur va faire deviner
    while not valid_code(code,color): #cas ou le code du joueur ne respecte pas les conditions
        code = list(input("The player had enters an invalid code. The player enters a code to guess (R/G/B/Y) : ")) #on redemande un code
    for i in range(30): #nettoyer la console
        print('\n')
    count_ligne = 1
    end = 0
    print("You must find the code that is composed of 4 colors.") #affichage des règles
    print("Possible colors are Red, Green, Blue and Yellow.")
    print("On both sides of the board are randomly orders indicators :")
    print("- G for Good colors \n- M for Misplaced colors \n")
    display_bord(board)
    code_player = input('Enter your code : ') #le joueur entre un code pour deviner
    while True:
        for i in range(30): #nettoyer la console
                print('\n')
        if valid_code(code_player,color): #si le code est valide on entre dans la condition
            print("You must find the code that is composed of 4 colors.") #affichage des règles
            print("Possible colors are Red, Green, Blue and Yellow.")
            print("On both sides of the board are randomly orders indicators :")
            print("- G for Good colors \n- M for Misplaced colors \n")
            indicators = verify_code(code_player,code) #obtention des indicateurs de jeux
            place_in_board(board,code_player,count_ligne) #place le code du joueur dans le tableau
            place_in_board_indicators(board,code_player,code,count_ligne,indicators) #place le code du joueur dans le tableau
            display_bord(board)
            if code_player == ''.join(code): #cas où le joueur trouve le code, il gagne
                print("You win")
                break #fin de la boucle
            count_ligne += 1
            end += 1
            if end == end_game:  #cas pour la derniere ligne du plateau
                if ''.join(code) == code_player: #si le joueur gagne
                    print("You win")
                    break #fin de la boucle
                else: #cas où le joueur perd
                    print(f'You lost... The code were {''.join(code)}')
                    break #fin de la boucle
            code_player = input('Enter your code : ') #demande au joueur un code
        else:
            code_player = input('Invalid input. Enter your code : ') #cas ou le code n'est pas valide