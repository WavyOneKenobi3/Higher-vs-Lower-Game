from gamedata import teams
import random

def comparison(): 
    score = 0
    
    A = random.choice(teams)   #random picks 2 dictionaries from list
    while True:
        B = random.choice([team for team in teams if team != A])
        if A['worth'] == B['worth']:
            B = random.choice([team for team in teams if team != A])
            
        print(f" {A['team']}, Sport: {A['Sport']}, From {A['city/country']}. ")
        print(f" {B['team']}, Sport: {B['Sport']}, From {B['city/country']}. \n")
         
        user_pick = input("Which Sports Team is worth more? A or B. ").lower()
        
            
        if user_pick == 'a'and A['worth'] > B['worth']:
            print("Correct! ")  
            score += 1
            print(f" {A['team']}, {A['worth']} Billion, Sport: {A['Sport']}, From {A['city/country']}. ")
            print(f" {B['team']}, {B['worth']} Billion, Sport: {B['Sport']}, From {B['city/country']}. \n")
        elif user_pick == "b" and A["worth"] < B["worth"]:
            print("Correct! ")
            print(f" {A['team']}, {A['worth']} Billion, Sport: {A['Sport']}, From {A['city/country']}. ")
            print(f" {B['team']}, {B['worth']} Billion, Sport: {B['Sport']}, From {B['city/country']}. \n")
            score +=1
            A = B 
        else: 
            print(f"Wrong answer, {A['worth']} Billion and {B['worth']} Billion. ")
            break
    print(f"Your score is {score}! ")            


comparison()
