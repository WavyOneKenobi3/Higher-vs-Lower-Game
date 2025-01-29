from gamedata import teams
import random

'''def team_select():
    for x in teams:                             #loop thru teams list
        for key,value in x.items():             #select keys and values from dict. selected
        
            
            
            
            
            
            
team_select()'''


def comparison(): 
    A, B = random.sample(teams, k=2)    #random picks 2 dictionaries from list
    print(f" {A['team']}, {A['worth']} Billion, Sprot: {A['Sport']}, From {A['city/country']}. ")
    print(f" {B['team']}, {B['worth']} Billion, Sprot: {B['Sport']}, From {B['city/country']}. ")
    while True:
        user_pick = input("Which Sports Team is worth more? A or B").lower()
        if user_pick == 'a':
            if A["worth"] > B["worth"]:
                print("Correct! ")  
            else: 
                print(f"Wrong answer, {A['worth']} Billion and {B['worth']} Billion. ")
                break
            B = random.sample(teams, k=1)
            print(f" {A['team']}, {A['worth']} Billion, Sprot: {A['Sport']}, From {A['city/country']}. ")
            print(f" {B['team']}, {B['worth']} Billion, Sprot: {B['Sport']}, From {B['city/country']}. ")
        elif user_pick == "b":
            if A["worth"] < B["worth"]:
                print("Correct! ")
            A == B 
            B == random.sample(teams, k=1)
            print(f" {A['team']}, {A['worth']} Billion, Sprot: {A['Sport']}, From {A['city/country']}. ")
            print(f" {B['team']}, {B['worth']} Billion, Sprot: {B['Sport']}, From {B['city/country']}. ")
        else: 
            print(f"Wrong answer, {A['worth']} Billion and {B['worth']} Billion. ")
            break
            


comparison()
'''
- which sports team is worth?
	
		- comparison line: team, worth, sport, city/country
	- comparing the teams
		- make A vs B, once get it right change B to A then B is a different team
	- letting the user choose between
	- function deciding right and wrong
	- add a counter on how many you got right, then once lost end game'''