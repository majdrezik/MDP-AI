"""
@author: Majd Rezik
@author: Oudai Salameh
"""

import numpy as np


#Hyperparameters
SMALL_ENOUGH = 0.005
GAMMA = 0.9        
NOISE = 0.1  



#actions={'right','wrong','leave'}
actions=[0 , 1 , 2]

#states={'1','2','3','4','5','6','7','8','9','10','loose','quit','winner'}

# 11 == loose   12 == quit
states=[1,2,3,4,5,6,7,8,9,10,11,12]
#Define rewards for all states
rewards = [1,5,10,50,100,500,1000,5000,15000,75000, 0]    

"""
return the reward of performing action 'a' given state 's'
"""      
def reward(s,a):
    totalRewards = 0
    loseTotalRewards =0
    if a == 2:
        for st in range(0,s):
            totalRewards += rewards[st]
        return totalRewards
    elif a==1:
         for st in range(0,s):
            loseTotalRewards -= rewards[st]
         return loseTotalRewards
    return rewards[s]


"""
return valid actions for state 's'
"""   
def actions(s):
    if s == 11 or s == 12 or s == 13:
        return {-1}
    return actions

#Define an initial policy
policy=[]
for s in range(13):
    policy.append(actions(s))
        


# each row is a different state (row 0 = state 1)
"""
transitions is a 2D array that holds the probabilities for each state(row)-action(col) 
""" 
transitions = [
#Pr. right wrong leave
    [0.99, 0.01 , 1], #from state 1 (index 0)
    [0.9, 0.1 , 1], #from state 2
    [0.8, 0.2 , 1], #from state 3
    [0.7, 0.3 , 1], #from state 4
    [0.6, 0.4 , 1], #from state 5
    [0.5, 0.5 , 1], #from state 6
    [0.4, 0.6 , 1], #from state 7
    [0.3, 0.7 , 1], #from state 8
    [0.2, 0.8 , 1], #from state 9
    [0.1, 0.9 , 1], #from state 10 (index 9)
#    [0, 0, 0]  #state 11 loose (index 10)
#    [0, 0, 0]  #state 12 quit (index 11)
    ]
    


"""
return the new state, given initial state 's' and action 'a'
""" 
def getStateFromTransition(s, a):
    if a == 0: #'right':
        return s+1 #if answered right, move to the next state (next question)
    elif a == 1: #'wrong':
        return 11
    elif a == 2: #'leave':
        return 12


"""
return the probability given initial state 's' and action 'a'
""" 
def getProbFromTransition(s,a):    
    if a == 0: #'right':
        return transitions[s][0] #if answered right, move to the next state (next question)
    elif a == 1: #'wrong':
        return transitions[s][1]
    elif a == 2: #'leave':
        return transitions[s][2]
    
"""
U is a vector of utilities for each state, initially zero.
policyList is a vector of best policy indexed by state, initially zero.
""" 
U = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
policyList = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}

"""
calculate the utility for each (s,a,s') as UtilityWin, UtilityLose, UtilityQuit
and save the maximum utility among them in U[s] list that is initialized '0' then choose the best policy for
each state according to the utilities.
""" 
def calculate():
    for s in range(len(states)-2):
        #print('calculating ', str(s))
        UtilityWin = calculateUtility(getProbFromTransition(s,0), reward(s,0), GAMMA, U[0 if s==0 else s-1])    #win
        UtilityLose = calculateUtility(getProbFromTransition(s,1), reward(s,1), GAMMA, U[0 if s==0 else s-1])   #loose
        UtilityQuit = calculateUtility(getProbFromTransition(s,2), reward(s,2), GAMMA, U[0 if s==0 else s-1])   #quit
        maxUtility = max(UtilityWin, UtilityLose, UtilityQuit)
        U[s] = maxUtility
        if maxUtility == UtilityWin: 
            policyList[s] = 0
        elif maxUtility == UtilityLose:
            policyList[s] = 1
        elif maxUtility == UtilityQuit:
            policyList[s] = 2
#    best_policy(U)
        
   
"""
helper functin that calculates a utility
"""  
def calculateUtility(prob, reward, gamma, previousUtility):
    return prob*(reward + gamma*previousUtility)
     
   
"""
given state 's', return the best policy of that state.
"""        
def best_action(s):
    return policyList[s-1]





