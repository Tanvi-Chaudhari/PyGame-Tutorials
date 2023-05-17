
# DARK FOREST MADE BY LAYERS

import pygame
  
pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Dimensions of the screen
WIDTH, HEIGHT = 900, 800
  
# Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
  
font = pygame.font.Font('freesansbold.ttf', 15)
  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parallax World")

# Define game variables
scroll = 0

ground_image = pygame.image.load("plx-7-8.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

# List of all background images
bg_images = []
for i in range(1, 7):
    bg_image = pygame.image.load(f"plx-{i}-8.png").convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT)) # Scale the image to match screen dimensions
    bg_images.append(bg_image)

# Get the width of each image i.e. is same.
bg_width = bg_images[0].get_width()

# For drawing the images
def draw_bg():
    for x in range(5):
        speed=1 
        for i in bg_images:
            screen.blit(i, ((x*bg_width)-scroll*speed, 0)) # Puts all images at this point/coordinate on top of each other and x*bg_width continues the BG in x direction.
            speed+=0.3 # With speeding, it looks fire dude!

def draw_ground():
    for x in range(15):
        # Damn, this really looks like I'm in train
        screen.blit(ground_image, ((x*ground_width)-scroll*4.2, HEIGHT - ground_height)) # Puts the ground on top of all images

# Loop required to keep the window from closing.
run = True
while run:

    clock.tick(FPS)

    #draw world
    draw_bg()
    draw_ground()

    # Get keypresses
    key = pygame.key.get_pressed()
    if(key[pygame.K_LEFT] and scroll>0): # This will not go to the left side.
        scroll -=5
    if(key[pygame.K_RIGHT] and scroll<3000): # This is like the game is going in right direction
        scroll +=5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()