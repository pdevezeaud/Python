#importation des bibliotheque necessaire
import pygame



#initialisation de la bibliotheque Pygame
pygame.init()

#créqtion de la fenetre
fenetre = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Space Invaders")
icone = pygame.image.load('ufo.png')
pygame.display.set_icon(icone)

#Initialisation du player
playerImg = pygame.image.load('player.png')
#positionnement du joueur sur la fenetre
playerx = 370
playery = 480
playerx_change = 0

def player(x,y):
    fenetre.blit(playerImg, (x, y))


#GameLoop
#initialisation de la variable running si true tourne sinon false et s'arrete
running = True

#boucle de jeu infini pour rafraichir la fenetre
while running:

     # RGB + RED  GREEN  BLUE
    fenetre.fill((0,0,0))

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0


    playerx += playerx_change

    #on lance la méthode
    player(playerx,playery)

    pygame.display.update()

    #48;10

