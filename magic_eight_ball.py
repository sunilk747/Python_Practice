import time, sys
from random import randint

responses = ("I don't know", "Yes", "Not a chance", "Nope", "Definitely", "Why would you ask me that?",
            "The answer is somewhere between yes and no", "Maybe", "Why don't I ask you a question now?",
            "Pancakes.", "Waffles.")
thinking = ("Hmm", "Hmmmmmm", "Let me think", "Uhh", "Well")

def main():
    print "Magic 8 ball: ask anything."
    while True:
        raw_input()
        showThinking()
        print(responses.__getitem__(randint(0, 10)))
        print "What else would you like to ask?"

def showThinking():
        sys.stdout.write(thinking.__getitem__(randint(0, 4)))
        time.sleep(0.7)
        sys.stdout.write('.')
        time.sleep(0.6)
        sys.stdout.write('.')
        time.sleep(0.5)
        sys.stdout.write('.')
        time.sleep(0.4)
        print

main()