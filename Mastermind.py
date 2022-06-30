#Carson James last edited on 6/29/2022
#This is a python version on the game mastermind
#The imports are for random number generation and number rounding
import random
import math



#This is an introduction and explains the rules to the player
print("Hello, welcome to mastermind, the goal of the game is to guess the number in a certain amount of guesses you will be told if the number is in the correct position or if the number is correct but not in the correct position")

#This boolean is used to make it so the game can continue after it is beaten
PlayAgain = True

#This while loop is 
while PlayAgain == True:

    #These declare variables for the correct position and correct number
    CorPos = 0
    CorNum = 0

    #This sets up the boolean for the game so the game can run after one turn
    GameWon = False

    #These set up the game by getting the number of guesses through user input and creates the random digits that makes the mystery number
    Numturns = int(input("How many guesses would you like? "))

    #This if and while loop is for players who try to break the code
    if Numturns < 1:
        while Numturns < 1:
            Numturns = int(input("Please enter a positive number that isn't 0, how many guesses would you like?"))
  
    #This is for storing the user input for later use
    RNumturns = int(Numturns)
    
    #This list is the range of the 4 digits
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   
    
    #These 4 functions select a random number from the lists and then set them to variables
    rand1 = int(random.choice(list1))
    rand2 = int(random.choice(list1))
    rand3 = int(random.choice(list1))
    rand4 = int(random.choice(list1))
    
    #This equation makes the mystery number to be used
    Mystery = int((rand1 * 1000) + (rand2 * 100) + (rand3 * 10) + rand4)
   
    #This is for making the mystery number is always for digits
    format(Mystery, "04")
    #print(Mystery)
    
    #This is the main game the loop continues until the RNumturns varaible is 0 or if the play wins by guessing the correct number
    while RNumturns > 0 and GameWon == False:
   
    #This gets the players guess
        Guess =int(input("Please input a positive 4 digit number "))

        #This if statement and while loop is for people who try to break the code 
        if Guess < 0:
            while Guess < 0:
                Guess = int(input("Please input a positive 4 digit number "))
       
        #These equations are for number isolation with a mix of modulo and division the math.floor function is to make it a whole number and round down to prevent any errors with comparing
        #This isolates the number in the 1000th position
        Guessp1 = Guess /1000
        Guessp1 = math.floor(Guessp1)
        #print(Guessp1) debugging
        
        #This isolates the number in the 100th position
        Guessp2 = (Guess / 100) % 10
        Guessp2 = math.floor(Guessp2)
        #print(Guessp2) debugging
        
        #This isolates the number in the 10th position
        Guessp3 = (Guess % 100)/10
        Guessp3 = math.floor(Guessp3)
        #print(Guessp3) debugging
       
        #This isolates the number in the 1st position
        Guessp4 = (Guess % 10)
        Guessp4 = math.floor(Guessp4)
        #print(Guessp4) debugging
       
        #These if statements are for checking if the player got any correct numbers if they do the appropriate varaible will increase
        #These statements are for the correct position
        if rand1 == Guessp1:
            CorPos = CorPos + 1
            # print("1 Working") debugging
       
        if rand2 == Guessp2:
            CorPos = CorPos + 1
           # print("2 working") debugging
       
        if rand3 == Guessp3:
            CorPos = CorPos + 1
           # print("3 working") debugging
       
        if rand4 == Guessp4:
            CorPos = CorPos + 1
            #print("4 working") debugging
       
        #These statements are for the correct number but not the correct position
        if Guessp1 != rand1 and Guessp1 == rand2 or Guessp1 == rand3 or Guessp1 == rand4:
            CorNum = CorNum + 1
        if Guessp2 != rand2 and Guessp2 == rand1 or Guessp2 == rand3 or Guessp2 == rand4:
            CorNum = CorNum + 1
        if Guessp3 != rand3 and Guessp3 == rand1 or Guessp3 == rand2 or Guessp3 == rand4:
            CorNum = CorNum + 1
        if Guessp4 != rand4 and Guessp4 == rand1 or Guessp4 == rand2 or Guessp4 == rand3:
            CorNum = CorNum + 1
       
        #These are debugs in case the combined value of the correct number and position go over 4
        TotalNum = CorNum + CorPos
        if TotalNum == 5:
            CorNum = 1
        if TotalNum == 6:
            CorNum = 1
        if TotalNum == 7:
            CorNum = 0
        if TotalNum == 8:
            CorNum = 0
       
        #These print statements are after the calculations and tell the player how close they were to mystery number the 4 different if statements are for grammar reasons
        if CorNum == 1 and CorPos > 1 or CorPos == 0:
            print("You have ", CorNum, " correct number and ", CorPos, " are in the correct position")
        if CorNum > 1 or CorNum == 0 and CorPos > 1 or CorPos == 0:
            print("You have ", CorNum, " correct numbers and ", CorPos, " are in the correct position")
        if CorNum == 1 and CorPos == 1:
            print("You have ", CorNum, " correct number and ", CorPos, " is in the correct position")
        if CorNum > 1 or CorNum == 0 and CorPos == 1:
            print("You have ", CorNum, " correct numbers and ", CorPos, " is in the correct position")

        #This equation makes the game countdown so that there is a way to loose
        RNumturns = RNumturns -1
        
        #This if statement is for if the player won the game by their guess being correct
        if CorPos == 4:
            #This equation shows how many turns it took for the player to get the correct number
            Remaining = Numturns - RNumturns
            #This if statement is for grammar purposes in chance the player guesses the mystery number in one turn
            if Remaining == 1:
                print("Congratulations you guessed the correct number ", Mystery, " in ", Remaining, " turn which means you've won the game")
            if Remaining > 1:
            #This if statement is for everything above one
                print("Congratulations you guessed the correct number ", Mystery, " in ", Remaining, " turns which means you've won the game")
            GameWon = True
        if RNumturns == 0:
            print("Sorry but you weren't able to guess the correct number ", Mystery)
        
        #These reset the CorNum and CorPos varaible at the end of each guess so the code does not store the number increase from the previous attempts
        CorNum = 0
        CorPos = 0
    
    #This is for playing the game again
    #This gets the user input for if the player wants to play again 1 and 0 are used due to problems with string comparison
    Question = int(input("Would you like to play again? Press 1 to play again or press 0 to quit"))
    
    #This while loop is for players trying to break the code
    while Question > 1 or Question < 0:
        if Question > 1 or Question < 0:
            
            #This is for anyone who tries to input a different answer than the expected one
            print("Please answer with 1 or 0")
            Question = int(input("Would you like to play again?"))
            
            #This is so the loop can break and the game can end
            if Question == 0:
                PlayAgain = False

#This print statment is for when to game ends it also helps to know that the program has gone through it also references how old aracade games would have a game over screen
print("Game Over")