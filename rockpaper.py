#Morgan Pickens
#3 Oct 2023
#HW5
#Rock, Paper, Scissors

#This is For Section 2 Random Computer choice
                         #Section 1
import random

# This is to make a global variable for any of my functions to use 
choices = {
        0: "Rock",
        1: "Paper",
        2: "Scissors"
    }

def Function_User_Choice():
    #This is the introduction to the Program and the Instructions to play 
    print("Hello and welome to Rock,Paper,or Scissors :). ")
    print("Instructions: Please type R or 0 for rock. ")
    print("              Please type P or 1 for Paper. ")
    print("              Please type S or 2 for Scissors. ")

    #This is For the user to pick his choice
    choice = input("Please input your choice. ")

    #These are my output variable strings
    R = "Rock"
    r = "Rock"
    P = "Paper"
    p = "Paper"
    S = "Scissors"
    s = "Scissors"

    #This is if the user chooses to use 0 1 or 2 
    input_mapping = input_mapping = {'R': 0, 'r': 0, 'P': 1, 'p': 1, 'S': 2, 's': 2, '0': 0, '1': 1, '2': 2}

    # Check if the user's input is valid
    # Check if the user's input is valid
    if choice in input_mapping:
        user_choice = input_mapping[choice]
        if user_choice == 0:
            print("You chose Rock")
        elif user_choice == 1:
            print("You chose Paper")
        elif user_choice == 2:
            print("You chose Scissors")
        return user_choice    
    else:
        print("Invalid input. Please choose 'R', 'P', 'S', 'r', 'p', 's', '0', '1', or '2.")
        return None 
#########################################################################################
#The above Portion is the end of our choice option of the progam.
#Next we will move on to the Devlopment of the actual Game.
    #Import random will be added to the top of my code here.
    #But it is for Section 2 and My Variables 
################################################################################

                           #Section 2
def Function_Computer_Choice():
     #This is for the computer to randomly make a choice
    compChoice = random.choice([0, 1, 2])
    print(f"Computer chose: {choices[compChoice]}")
    return compChoice

################################################################################
#and Boom section 2 is finished! are you as shocked as i am?
#To create a random computer chose only took 2 lines of code!
#Lets move onto section 3
#Section 3 will up us define our choices
################################################################################

                           #Section 3
def Function_WhoIsTheWinner(user_choice, compChoice):
    if user_choice == 0:  # If you choose Rock
        if compChoice == 1:  # Computer chooses Paper
            print("Computer Wins")
        elif compChoice == 2:  # Computer chooses Scissors
            print("You Win")
        else:
            print("It's a Tie")

    elif user_choice == 1:  # If you choose Paper
        if compChoice == 0:  # Computer chooses Rock
            print("You Win")
        elif compChoice == 2:  # Computer chooses Scissors
            print("Computer Wins")
        else:
            print("It's a Tie")

    elif user_choice == 2:  # If you choose Scissors
        if compChoice == 0:  # Computer chooses Rock
            print("Computer Wins")
        elif compChoice == 1:  # Computer chooses Paper
            print("You Win")
        else:
            print("It's a Tie")

    # This section is for user choice of R and r
    elif user_choice in ['R', 'r']:  # If you choose Rock
        if compChoice == 1:  # Computer chooses Paper
            print("Computer Wins")
        elif compChoice == 2:  # Computer chooses Scissors
            print("You Win")
        else:
            print("It's a Tie")

    # This section is for P and p
    elif user_choice in ['P', 'p']:  # If you choose Paper
        if compChoice == 0:  # Computer chooses Rock
            print("You Win")
        elif compChoice == 2:  # Computer chooses Scissors
            print("Computer Wins")
        else:
            print("It's a Tie")

    # This section is for S and s
    elif user_choice in ['S', 's']:  # If you choose Scissors
        if compChoice == 0:  # Computer chooses Rock
            print("Computer Wins")
        elif compChoice == 1:  # Computer chooses Paper
            print("You Win")
        else:
            print("It's a Tie")

##############################################################################################
        #Hurray we did it!
        #At the end of this section i have no relized i did not turn Code into funcitons
        #So i will do that now and then add my Main function for seciton4
##############################################################################################

                        #Section 4: The main Function
           
def main():
    user_choice = Function_User_Choice()
    if user_choice is not None:
        compChoice = Function_Computer_Choice()
        Function_WhoIsTheWinner(user_choice, compChoice)

if __name__ == "__main__":
    main()
                       #Quesiton Section
#How did i approach this assignment? I approached this assignment by analyzing
#The requriments and cutting them into sections

# Where did i get stuck? I got stuck making the main function i had to go back
# and edit alot of my work in order for it to work

#What did i learn from this assignement?
#I leanred how to create a gam elike rock paper scissors. 
