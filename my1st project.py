import random

def choose():
    words=['science', 'computer', 'register', 'variables', 'constants', 'syntax', 'tuples', 'dictionaries', 'Accumulator', 'import', 'string', 'turtle', 'anaconda', 'while', 'lists']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,"Your score is=",p1)
    print(p2n,"Your score is=",p2)
    print("Thanks for playing")
    print("Have a nice day")

def play():
    print("----------Welcome to the Computer Language Jumble Word Quiz--------------")
    p1name=input("Player 1,Please enter your name= ")
    p2name=input("Player 2,Please enter your name= ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer task to make question.
        picked_word=choose()
        qn=jumble(picked_word)
        if(turn%2==0):
            #player 1
            print(p1name,"It is tour turn.\n")
            print("Guess the word : ",qn)
            ans=input("What is on my mind?\n")
            if(ans==picked_word):
                print("YOU GUESSED IT RIGHT!!!")
                pp1=pp1+1
                print(p1name,"Your score is ",pp1)
            else:
                print("BETTER LUCK NEXT TIME. THE WORD WAS",picked_word)
            c=int(input("PRESS 1 TO CONTINUE AND 0 TO EXIT= "))
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
        else:
            #player 2
            print(p2name,"It is tour turn.\n")
            print("Guess the word : ",qn)
            ans=input("What is on my mind?\n")
            if(ans==picked_word):
                print("YOU GUESSED IT RIGHT!!!")
                pp2=pp2+1
                print(p1name,"Your score is ",pp2)
            else:
                print("BETTER LUCK NEXT TIME. THE WORD WAS",picked_word)
            c=int(input("PRESS 1 TO CONTINUE AND 0 TO EXIT= "))
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
play()
