import pygame as pg

usedWords = []
targetWord = ["f", "r", "a", "n", "k"]

def guessWord(guess):
    final = []
    
    for i in range(5):
        if guess[i] == targetWord[i]:
            final.append(guess[i])
        elif guess[i] != targetWord[i] and guess[i] in targetWord:
            final.append(guess[i].upper())
        else:
            final.append("_")


        if final == targetWord:
           return (final)
                    
        elif(len(final) == 5):
            # print("your guess")
            # print(final)
            # print("-------------")
            # print("wrong letters")
            return final

    return final

def checkWord(guess):
    final = []

    for i in range(5):
        if guess[i] == targetWord[i]:
            final.append(guess[i])
            final.append(" ")
        elif guess[i] != targetWord[i] and guess[i] in targetWord:
                final.append(guess[i].upper())
                final.append(" ")
        else:
            final.append("_ ")

            
    
    return "".join(final)


def main():
    found = False

    pg.display.set_caption("Wordle")

    screen = pg.display.set_mode((500, 400))
    font = pg.font.Font(None, 32)
    font2 = pg.font.Font(None, 40)
    input_box = pg.Rect(150, 300, 200, 32)
    color_inactive = pg.Color('grey')
    color_active = pg.Color('black')
    color = color_inactive
    active = False
    text = ''
    running = True
    guesses = 5

    while running:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                
                # Change the current color of the input box.
                color = color_active if active else color_inactive

                # if they press a key and its active and there is guesses left
            if event.type == pg.KEYDOWN and active and guesses > 0:
                
                if event.key == pg.K_RETURN:
                    usedWords.append(text)
                   
                    guesses -= 1
                    attemptedWord = guessWord(text)
                    print(attemptedWord)

                    if attemptedWord == targetWord:
                        found = True
                    
                    text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            
            
            elif guesses < 1:
                text = "        you lose"
                color = pg.Color("red")
               
            
        if found == True:
            text = "        you win"
            color = pg.Color("green")
    

        screen.fill((220, 220, 220))


        # Render the current text.
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pg.draw.rect(screen, color, input_box, 2)


        usedWordsX = 200
        usedWordsY = 50
        for words in usedWords:
             # Render the current text.
            txt_surface = font2.render(checkWord(words), True, "black")
            # Blit the text.
            screen.blit(txt_surface, (usedWordsX, usedWordsY))
            usedWordsY += 40
            # Blit the input_box rect.

        pg.display.flip()


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()