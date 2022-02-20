"""
@author: Majd Rezik
@author: Oudai Salameh

@Professor: Miri Weiss Cohen

Submission Date: 20.2.2022

AI course final project 2022 semester A.

"""


import random
import time
import sys
import re
from MDP1 import *


global rewards, question, answers, i, f, totalReward, selectedAnswer, questionList, userName, fileName, answersDictionary
fileName = "Questions.txt"
userName = input("Hello, welcome to our AI Course MDP Game, What is your name?" + "\n")
totalReward =0
wantsToContinue = 'q'
chosenQuestions = []

#call introduction function
def intro(name):
   print("\nWelcome again " + name + " to the game :" + "\n"+
   "You are asked a multiple choice question, with four options <A>, <B>, <C> and <D> only!." +
   "If you answer correctly, you earn rewards accordingly and get to decide wether:" +
   "to move onto the next question <Y> and take risks or to quit <Q> with the rewards you gained till this round" +
   "If you answer incorrectly then you lose the all rewards you have earned." +
   "P.S. The questions will become more difficult as you progress, so be ready for it !" +
   "\nLet the Round Begin" + "\n" + "________________________________________\n\n")
   time.sleep(2)


"""
printSuggestions prints the suggestions of the MDP model whether the user should continue or quit.
"""
def printSuggestions():
    if best_action(i+1) == 2:
        print("\n\n*******  the model suggests you to quit.  ******* \n")  
    if best_action(i+1) ==1:
        print("\n\n*******  High chance of loosing!  ******* \n")  
    if best_action(i+1) == 0:
        print("\n\n*******  the model suggests you to continue.  ******* \n")
    print("would you wish to continue<Y> or quit <Q>?")

"""
isRightAnswer returns true if the user chose the right answer to the given question.
"""
def isRightAnswer(expectedAnswer, selectedAnswer):
    return selectedAnswer ==  expectedAnswer


"""
isValidAnswer returns true if the user input a valid answer.
"""
def isValidAnswer(selectedAnswer):
	if len(selectedAnswer) > 1 or selectedAnswer!='A' and selectedAnswer!='B' and selectedAnswer!='C' and selectedAnswer!='D'and wantsToContinue!='Y' and wantsToContinue!='Q' and wantsToContinue!='y' and selectedAnswer !='a'and selectedAnswer !='b'and selectedAnswer !='c'and selectedAnswer !='d':
	    return False
	return True
		

intro(userName)

i = 1
j = 0

rewards = [1,5,10,50,100,500,1000,5000,15000,75000, 0]  


"""
calculate starts the mdp model to suggest the user whether they should continue
"""
calculate()


"""
start choosing random questions from the questions file
"""
while i <= 10:
   questionList = list(open(fileName)) 
   f = questionList.pop(random.randint(0,len(questionList) - 1))
   print('\nQuestion:', i, "for", str(rewards[i-1])+'$')
   lines = f.split('[')
   question = lines[0]
   """
   while we're poping a question we already had, choose another question.
   """
   while question in chosenQuestions:
        f = questionList.pop(random.randint(0,len(questionList) - 1))
        lines = f.split('[')
        question = lines[0]
   """
   add the question to the list so we never use it again.
   """
   chosenQuestions.append(question)
   answers = lines[1].strip("\n").split(',')
   time.sleep(1)
   print(question)
   for j in range(4):
       a = 'A'
       a = ord(a[0]) + j
       a = chr(a)
       print(a , ": " + answers[j])
       time.sleep(1)

   selectedAnswer = input("Please answer " + userName + ":\n")
   selectedAnswer = selectedAnswer.upper()
	
   while isValidAnswer(selectedAnswer) == False:
	    print('Invalid answer, please choose "A", "B", "C", "D"')
	    selectedAnswer = input("Please answer " + userName + ":\n")
	    selectedAnswer = selectedAnswer.upper()
       
   answersDictionary = {'A' : answers[0],'B' : answers[1], 'C' : answers[2], 'D' : answers[3]}     
   if selectedAnswer in answersDictionary:
       """
       if the user chose the right answer (answers[4] is the right answer in the questions file.)
       """
       if answersDictionary[selectedAnswer] == answers[4]:
           print('\n' + 'That is the correct answer.' + "\n")
           time.sleep(1)
           totalReward += rewards[i-1]
           if i < 10:
               printSuggestions()
               wantsToContinue = input ("Please answer  "+ userName + ":\n")
               wantsToContinue = wantsToContinue.upper()
               if wantsToContinue == 'Q' or wantsToContinue == 'q':
                   print("Goodbye, total reward is :"+ str(totalReward))
                   break
               elif wantsToContinue == 'Y' or wantsToContinue == 'y':
                   print("Continuing, current reward is :"+ str(totalReward) + "\n")
               if i > 6:
                   print("You are one step closer to finish the game." + "\n")
           elif i == 10:
               print("Congratulations. You won the game!")
               time.sleep(5)
               break
       else:
               print('Too bad ' + userName  + ', Game over. The right answer is', str(answers[4]) + "!")
               break
   i = i + 1
	
    
    
 