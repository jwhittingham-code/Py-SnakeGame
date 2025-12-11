from Settings import *


#---------------------------------------------------------------
class MenuSelect(Enum):
    Start = 0
    Exit = 1
global menuState
menuState = MenuSelect.Start

#---------------------------------------------------------------

def menu(font,font2,moveSound,selectSound):
    
    colourSelect = "white"
    colourOther = (100,100,100)


    
    textsurf = font.render("Py-Snake",True,(30,30,30))
    textrect = textsurf.get_frect(center = (w_Width/2 , w_Height/3))
    
    

    global menuState
    match menuState:
        case MenuSelect.Start:
            startColour = colourSelect
            exitColour = colourOther
        case MenuSelect.Exit:
            startColour = colourOther
            exitColour = colourSelect
    
    starttextsurf = font2.render("play",True,startColour)
    starttextrect = starttextsurf.get_frect(center = (w_Width/2,w_Height/2 + 100))
    exittextsurf = font2.render("exit",True,exitColour)
    exittextrect = exittextsurf.get_frect(center =(w_Width/2, w_Height/2 + 150))
    
    displaySurf.blit(textsurf,textrect)
    displaySurf.blits([(starttextsurf,starttextrect),(exittextsurf,exittextrect)])
    
    keyinput = pygame.key.get_just_pressed()
    if keyinput[pygame.K_SPACE]or keyinput[pygame.K_RETURN]:
        selectSound.play()
        if menuState == MenuSelect.Start:
            return GameState.Play
        elif menuState == MenuSelect.Exit:
            return GameState.GameOver
    
    elif keyinput[pygame.K_DOWN] or keyinput[pygame.K_UP]:
        moveSound.play()
        match menuState:
            case MenuSelect.Start:
                menuState = MenuSelect.Exit
            case MenuSelect.Exit:
                menuState = MenuSelect.Start
        return GameState.MainMenu
    
    else:
        return GameState.MainMenu
       
    




        