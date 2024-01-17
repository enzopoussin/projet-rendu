from game import * #importation des fonctions player_vs_player et player_vs_computer

def menu():
    '''
    This function displays the game menu
    :return: None
    '''
    for i in range(30):  # nettoyer la console
        print('\n')
    while True: #tant que c'est vrai afficher le menu
        print("------------------------------------------") #affichage du menu
        print("         Welcome to the Mastermind        ")
        print("------------------------------------------\n\n")
        print('You will have the right to choose a difficulty level :')
        print("-EASY : 12 attempts \n-MEDIUM : 8 attempts \n-HARD : 5 attempts")
        choice = input('Do you wan to play against a Player or the Computer ? (C/P) : ') #choix pour jouer contre ordi ou joueur
        while choice != 'C' and choice != 'P': #cas si le choix n'est pas P ou C
            choice = input('Sorry I did not understand, enter P for Player and C for Computer : ') #on redemande un choix
        if choice == 'C': #si le choix est C
            choice_difficulty = input('Choose the difficulty \n-Press 1 for EASY \n-Press 2 for MEDIUM \n-Press 3 for HARD \n choice : ') #on demande la difficulté
            while choice_difficulty != '1' and choice_difficulty != '2' and choice_difficulty != '3': #cas ou l'entrée du joueur ne respecte pas les conditions on remande un coed
                choice_difficulty = input('Sorry I did not understand.. \n-Press 1 for EASY \n-Press 2 for MEDIUM \n-Press 3 for HARD \n choice :')
            player_vs_computer(the_end(choice_difficulty), choice_board(choice_difficulty)) #lancement du jeu
            choice_end = input("Press Q for return to menu or P to play : ") #choix de la fin si retour menu ou rejouer
            while choice_end != 'Q' and choice_end != 'P': #cas ou l'entrée ne correspond pas on redemade un code
                choice_end = input('Sorry I did not understand, enter Q for return to menu and P for play : ')
            while choice_end == 'P': #tant que le joueur choisit de jouer
                choice_difficulty = input('Choose the difficulty \n-Press 1 for EASY \n-Press 2 for MEDIUM \n-Press 3 for HARD \n choice : ') #choix de la difficulyté
                while choice_difficulty != '1' and choice_difficulty != '2' and choice_difficulty != '3': #cas si l'entrée ne respecte pas les condtitions on redemande un code
                    choice_difficulty = input('Sorry I did not understand.. \n-Press 1 for EASY \n-Press 2 for MEDIUM \n-Press 3 for HARD \n choice :')
                else:
                    player_vs_computer(the_end(choice_difficulty), choice_board(choice_difficulty)) #sinon on lance la fonction du jeu
                choice_end = input("Press Q for return to menu or P to play : ") #on redemande si le joueur veut retourner au menu ou jouer
                while choice_end != 'Q' and choice_end != 'P':
                    choice_end = input('Sorry I did not understand, enter Q for return to menu and P for play : ')
            else:
                menu() #lance le menu si le joueur a entré Q

        else: #cas ou le joueur joue contre un autre joueur
            choice_difficulty = input('Choose the difficulty \n-Press 1 for EASY \n-Press 2 for MEDIUM \n-Press 3 for HARD \n choice : ') #choix de la difficulté
            while choice_difficulty != '1' and choice_difficulty != '2' and choice_difficulty != '3': #cas ou l'entrée ne respecte pas les conditions
                choice_difficulty = input('Sorry I did not understand.. \n-Press 1 for EASY \n-Press 2 for MEDIUM \n-Press 3 for HARD \n choice : ') #on redemande un choix
            player_vs_player(the_end(choice_difficulty), choice_board(choice_difficulty)) #lancement de la fonction de jeu
            choice_end = input("Press Q for return to menu or P to play : ") #choix retour au menu ou rejouer
            while choice_end != 'Q' and choice_end != 'P': #cas ou l'entrée ne respecte pas les conditions
                choice_end = input('Sorry I did not understand, enter Q for return to menu and P for play : ') #on remande un choix
            while choice_end == 'P': #tant que le joueur choisit de jouer
                choice_difficulty = input('Choose the difficulty \n-Press 1 for EASY \n-Press 2 for MEDIUM \n-Press 3 for HARD \n choice :') #demande une difficulté
                while choice_difficulty != '1' and choice_difficulty != '2' and choice_difficulty != '3': #cas où l'entrée ne respecte pas les conditions
                    choice_difficulty = input('Sorry I did not understand.. \n-Press 1 for EASY \n-Press 2 for MEDIUM \n-Press 3 for HARD \n choice :') #on redemande un choix
                else:
                    player_vs_player(the_end(choice_difficulty), choice_board(choice_difficulty)) #sinon on lance la fonction du jeu
                choice_end = input("Press Q for return to menu or P to play : ") #on redemande si le joueur veut retourner au menu ou jouer
                while choice_end != 'Q' and choice_end != 'P':
                    choice_end = input('Sorry I did not understand, enter Q for return to menu and P for play : ')
            else:
                menu() #lance le menu si le joueur a entré Q