<<<<<<< Updated upstream
import pygame
import time
import random

WIDTH, HEIGHT = 500, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Dodge')

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()
=======
import pygame
import time
import random

WIDTH, HEIGHT  = 500, 400
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space Dodge")

def main():
    run = True
    while run:
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
    pygame.quit 
if __name__=="__main__":
    main()
    
>>>>>>> Stashed changes
