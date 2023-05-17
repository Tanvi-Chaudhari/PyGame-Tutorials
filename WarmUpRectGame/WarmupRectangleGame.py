import pygame
  
pygame.init()
  
# Dimensions of the screen
WIDTH, HEIGHT = 800, 600
  
# Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
  
font = pygame.font.Font('freesansbold.ttf', 15)
  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Defining the color of rectangle named as player
player = pygame.Rect((300, 250, 50, 50))

# Loop required to keep the window from closing.
run = True
while run:

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]==True: # Moving Left
        player.move_ip(-1, 0) # Because I'm traveling in negative x direction and y coordinate is not affected. 
    elif key[pygame.K_w]==True: #Doubt
        player.move_ip(0, -1)
    elif key[pygame.K_d]==True:
        player.move_ip(1, 0)
    elif key[pygame.K_s]==True: #Doubt
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

# to control the frame rate
# clock = pygame.time.Clock()
# FPS = 30