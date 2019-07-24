#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:16:35 2019

@author: tkhodr
"""
from random import randint
# Rock, Paper, Scissors game by Talal K
# Your program should accept 6 inputs from a user:'r' for rock, 'p' for paper, 
# 's' for scissors and 'y' for yes and 'n' for no, 'sc' for score.
sc = (0)
rps = ["r","p","s"]



def game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please make a selection")
    player = False
    algo = rps[randint(0,2)]
    while player == False:    
        player = input("Choose from:r,p,s,y,n,sc >")
        if player == algo:
            print("TIE!")
        elif player == "r":
            if algo == "s":
                print("You Smashed the algorithim!")
                sc == sc+1
            else:
                print("You lost to something that doesnt have a brain...")
        elif player == "s":
            if algo == "p":
                print("You chopped up the algo!")
                sc == sc+1
            else:
                print("You just got wrecked")
        elif player == "p":
            if algo == "r":
                print("YOU COVERED THE ALGO!")
                sc == sc+1
            else:
                print("You just got covered up!")
        elif player == "sc":
            print(int(sc))
        elif player == "y":
            continue
        elif player == "n":
            break 

game()
        
    
    
