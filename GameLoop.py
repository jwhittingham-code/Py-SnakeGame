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
     #have learnt that I should have used more verbose variable names here so the loop is easier to read.
     #this also goes for player and follower pos variable as this is actually used to track each objects previous position.
    for x in range(len(followers)):
        y = x - 1
        
        #loop checks the current "followers" position againt the "follower" in front and updates position based on if its changed 
        #note also checks for the player as the followers list starts with the player.
        if player.pos != pygame.math.Vector2(player.rect.center):
            if x > 0: 
                if followers[x] != player and player.move == False:
                    # We are checking that we are not the player and if the player has moved
                    followers[x].rect.center = followers[y].pos
                    #We then set our position to the previous position of the object ahead in the followers list.
                    
                if player.move ==True:
                    #If player is moving we record current position so we can move following objects next time through this loop
                    followers[x].pos = followers[x].rect.center
                if x > 2:
                    if followers[x].rect.colliderect(player.rect):
                        player.collide = True
                        player.colour = 'red'
                        #quitPython()
                        

           