import sys
from random import randint

rock = 'r'
paper = 'p'
scissors = 's'
choices = [rock, paper, scissors]

def main():
    print "Let\'s play Rock Paper Scissors. Type \'r\' | \'p\' | \'s\' to start.\n"
    numTurns = 0

    while True:
        userMove = getUserMove()
        computerMove = getComputerMove()

        while userMove is 'invalid':
            print "Please enter a valid move (r/p/s) "
            userMove = getUserMove()

        getWinner(userMove, computerMove)
        displayScore()
        if numTurns == 0:
            # display this message only once
            print "Make another move (or \'q\' to exit): "
        numTurns += 1

def getWinner(user, comp):
    if user == comp:
        print "It's a tie!"
    elif user == rock and comp == paper:
        print "You lose: paper beats rock."
        computerWin()
    elif user == rock and comp == scissors:
        print "You win! Rock beats scissors."
        userWin()
    elif user == paper and comp == rock:
        print "You win! Paper beats rock."
        userWin()
    elif user == paper and comp == scissors:
        print "You lose: scissors beats paper."
        computerWin()
    elif user == scissors and comp == rock:
        print "You lose: rock beats scissors."
        computerWin()
    elif user == scissors and comp == paper:
        print "You win! Scissors beats paper."
        userWin()

def computerWin():
    global computerScore
    computerScore += 1

def userWin():
    global userScore
    userScore += 1

def displayScore():
    print "Wins: {}, Losses: {}".format(userScore, computerScore)

def getComputerMove():
    return choices.__getitem__(randint(0, 2))

def getUserMove():
    move = raw_input().lower()
    if move in choices:
        return move
    elif 'q' in move:
        print "\nThanks for playing!\n"
        sys.exit(0)
    else:
        return 'invalid'

userScore = computerScore = 0
main()