import random
import time
import sys
import linecache
import glob

def main():
    menu()

# This is the main menu, where every user will first load onto.
def menu():
    r = True
    while r == True:
        print("========================================================")
        print("***********|Welcome to The Tournament Menu|*************")
        print("========================================================")
        enter = input("\n[Press Enter To Continue] ")
        time.sleep(0.3)
        print("\nLoading...")
        time.sleep(0.5)
        choice = input('''
========================================================

    A: Individual Player Menu
    B: Team Menu
    C: Exit Menu
    
========================================================
\nPlease select what you wish to view: ''')
        if choice == "A" or choice == "a":
            playerMenu()
        elif choice == "B" or choice == "b":
            teamMenu()
        elif choice == "C" or choice == "c":
            exit()
        else:
            time.sleep(0.3)
            print("\nERROR! Please enter a valid choice.")
            menu2()
#
#
# This menu will loop, instead of the first one. As some components,
# do not have to be repeated such as the "Press Enter To Continue" and loading.
def menu2():
    
# This loop has been done to ensure that if an invalid choice is to be typed by mistake,
# the menu will load again with an error message.
    running = True
    while running == True:
        time.sleep(0.5)
        print("\n========================================================")
        print("************|Welcome to The Tournament Menu|************")
        print("========================================================")
        time.sleep(0.3)
        choice = input('''
========================================================

    A: Individual Player Menu
    B: Team Menu
    C: Exit Menu
    
========================================================
\nPlease select what you wish to view: ''')
# This IF statement will take the user to the player menu.
        if choice == "A" or choice == "a":
            playerMenu()
            break
# This ELIF statement will take the user to the team menu.
        elif choice == "B" or choice == "b":
            teamMenu()
            break
# This ELIF statement ends the program.
        elif choice == "C" or choice == "c":
            exit()
# This ELSE statement will loop back to the beginning of the menu if an invalid choice is inputted. 
        else:
            time.sleep(0.3)
            print("\nERROR! Please enter a valid choice.")
            running == True
#
#
# This is where the program will navigate the user if choice "A" is selected.
def playerMenu():
    runningplayer = True
    while runningplayer == True:
        time.sleep(0.7)
        print("\n====================================================")
        print("************|Welcome to The Player Menu|************")
        print("====================================================")
        time.sleep(0.5)
        choice = input('''
====================================================

    A: Add Player & Score
    B: Delete Player
    C: View Scores
    D: Back To Main Menu
    E: Exit Menu

====================================================
\nPlease select what you wish to do: ''')

# This ELIF statement will allow the user to write the name and score of the player.
        if choice == "A" or choice == "a":
            save_name = input('Enter your name: ').title()
            save_score = input('Enter your score: ')
            text_file = open("highscores.txt", "r")
            whole_thing = text_file.readlines()
            text_file.close()
            if len(whole_thing) < 40:
                text_file = open("highscores.txt", "a")
                text_file.write("\n" + save_name + ' | ' + save_score + "\n")
                text_file.close()
            text_file = open("highscores.txt", "r")
            whole_thing = text_file.read()
            time.sleep(0.5)
            print (whole_thing)
            text_file.close()
            
# This ELIF statement will allow the user to delete a player from the text file.
        elif choice == "B" or choice == "b":
            print("These are the current players and their score:")
            text_file = open("highscores.txt", "r")
            whole_thing = text_file.read()
            print(whole_thing)
            text_file.close()
            time.sleep(0.3)
            save_delete = input("Please enter the name of the player you wish to delete: ") + " | "
            #print(f"save_delete = {save_delete}")
            with open("highscores.txt", "r") as f:
                lines = f.readlines()
                #print(lines)
            with open("highscores.txt", "w") as f:
                for line in lines:
                    if not(line.startswith(save_delete)):
                        f.write(line)

# This ELIF statement will allow the user to view the scores of all players.
        elif choice == "C" or choice == "c":
            with open('highscores.txt', encoding = 'utf-8', mode = 'r') as my_file:
                file = open("highscores.txt", encoding='utf-8', mode='r')
                text = file.read()
                print(text)

# This ELIF statement will send the user back to the main menu.
        elif choice == "D" or choice == "d":
            menu2()

# This ELIF statement exits the entire program.
        elif choice == "E" or choice == "e":
            exit()

# This ELSE statement will loop back to the beginning of the player menu if an invalid choice is inputted.
        else:
            time.sleep(0.3)
            print("\nERROR: Please select a choice!")
            runningplayer == True
#
#
# This is where the program will navigate the user if choice "B" is selected.
def teamMenu():
    runningteam = True
    while runningteam == True:
        time.sleep(0.3)
        print("\n====================================================")
        print("*************|Welcome to The Team Menu|*************")
        print("====================================================")
        time.sleep(0.2)
        choice = input('''
====================================================
                                                    
    A: Add Team & Score                             
    B: Delete Team                                  
    C: View Scores                                  
    D: Back To Main Menu
    E: Exit Menu
                                                    
====================================================
\nPlease select what you wish to do: ''')

# This ELIF statement will allow the user to write the name and score of the team.
        if choice == "A" or choice == "a":
            save_name = input('Enter your team name: ').title()
            save_score = input('Enter your score: ')
            text_file = open("highscores.txt", "a")
            text_file.close()
            text_file = open("teamhighscores.txt", "r")
            whole_thing = text_file.readlines()
            text_file.close()
            if len(whole_thing) < 10:
                text_file = open("teamhighscores.txt", "a")
                text_file.write("\n" + save_name + ' | ' + save_score + "\n")
                text_file.close()
            text_file = open("teamhighscores.txt", "r")
            whole_thing = text_file.read()
            time.sleep(0.5)
            print (whole_thing)
            text_file.close()
            
# This ELIF statement will allow the user to delete a player from the text file.
        elif choice == "B" or choice == "b":
            print("These are the current teams and their score")
            text_file = open("teamhighscores.txt", "r")
            whole_thing = text_file.read()
            print(whole_thing)
            text_file.close()
            time.sleep(0.3)
            save_delete = input("Please enter the name of the player you wish to delete: ") + " | "
            # print(f"save_delete = {save_delete}")
            with open("teamhighscores.txt", "r") as f:
                lines = f.readlines()
                # print(lines)
            with open("teamhighscores.txt", "w") as f:
                for line in lines:
                    if not(line.startswith(save_delete)):
                        f.write(line)

# This ELIF statement will allow the user to view the scores of all teams.
        elif choice == "C" or choice == "c":
            with open('teamhighscores.txt', encoding = 'utf-8', mode = 'r') as my_file:
                file = open("teamhighscores.txt", encoding='utf-8', mode='r')
                text = file.read()
                print(text)

# This ELIF statement will send the user back to the main menu.
        elif choice == "D" or choice == "d":
            menu2()

# This ELIF statement exits the entire program.
        elif choice == "E" or choice == "e":
            exit()
        
# This ELSE statement will loop back to the beginning of the team menu if an invalid choice is inputted.
        else:
            time.sleep(0.3)
            print("\nERROR: Please select a choice!")
            runningplayer == True

main()
