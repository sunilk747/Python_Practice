import sys
from random import randrange

def main():
    showOptionsConfiguration()
    while True:
        followupInput = raw_input("Press \'r\' to reroll | \'c\' to re-configure | \'q\' to quit. ")
        if 'r' in followupInput:
            roll()
        elif 'c' in followupInput:
            showOptionsConfiguration()
        elif 'q' in followupInput:
            sys.exit(0)
        else:
            print "Please enter a valid command: "

def showOptionsConfiguration():
    global numDice
    numDice = int(raw_input("How many dice would you like to roll at a time? "))
    global numSides
    numSides = int(raw_input("How many sides are on each dice? "))
    roll()

def roll():
    numRolls = 0
    while numRolls < numDice:
        print str(randrange(1, numSides))
        numRolls += 1

main()