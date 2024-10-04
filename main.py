#!/usr/bin/env python 

import random 
import time
import os

number=7

play=input("Hello welcome to my game do you want to play?: ")

if play.lower()=="no" or play.lower()=="n":
    quit()
else:
    print("Ok so alright!")

def main():
    guess=int(input("Hey bro say your type your guess:  "))
    if guess==number:
        print("Bro you have guessed the word correctly")
        print("Ok my program has succeded in it's goal so bye")
        time.sleep(10)
        os.system("clear")
        quit()
    
    else:

	    print("So , you have not guessed the number correctly but you can try again bye")

main()


