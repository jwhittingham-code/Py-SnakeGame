import Settings
from Settings import *
import Player,Follower

#---------------------------------------------
def displayScore(player,font):
    score = player.points
    textSurf = font.render(str(score),True, (30,30,30))
    textrect = textSurf.get_frect(center = (w_Width/2 , w_Height/2))
    displaySurf.blit(textSurf,textrect)

def gameloop(player, followers):
     #updating and moving "followers"
    for x in range(len(followers)):
        y = x - 1
        s = 0.015
        
        if player.pos != pygame.math.Vector2(player.rect.center):
            if x > 0: 
                if followers[x] != player and player.move == False:
                    followers[x].rect.center = followers[y].pos
                if player.move ==True:
                    followers[x].pos = followers[x].rect.center
                if x > 2:
                    if followers[x].rect.colliderect(player.rect):
                        player.colour = 'red'
                        

           