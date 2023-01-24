import pygame
from pygame.locals import *

word = ["c", "l", "o", "c", "k"]
wrong_letters = []

def validateGuess(list):
    if(len(list) == 5):
        return True

    return False


def guessWord():
    guess = input("guess the word ")
    final = []
    

    for i in range(5):
        if validateGuess(guess):
            if guess[i] == word[i]:
                final.append(guess[i])
            elif guess[i] != word[i] and guess[i] in word:
                final.append(guess[i].upper())
            else:
                final.append("_")
                wrong_letters.append(guess[i])

            if final == word:
                print("word found :" + " ".join(final))
                return True
            
            elif(len(final) == 5):
                print("your guess")
                print(final)
                print("-------------")
                print("wrong letters")
                print(wrong_letters)
    
        else:
            print("invalid guess")
            return
            
    return False


def main():
    for i in range(5):
        attempt = guessWord()
        if(attempt == True):
            return "you win"
    
    return "you lose"

if __name__ == '__main__':
    pygame.init()
    print(main())