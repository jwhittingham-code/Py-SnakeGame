from Settings import *
#from main import state

def menu(font):
    textsurf = font.render("Menu",True,(30,30,30))
    textrect = textsurf.get_frect(center = (w_Width/2 , w_Height/2))
    displaySurf.blit(textsurf,textrect)
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        return GameState.Play
    else:
        return GameState.MainMenu
    print(key[pygame.K_SPACE])