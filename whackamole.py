import pygame
import random
darkGrey = pygame.Color(40, 40, 40)
creme = pygame.Color(204, 204, 153)


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((700, 572))
        clock = pygame.time.Clock()
        running = True
       
        #initial position of mole
        pt1 = random.randrange(33, 659, 32)
        pt2 = random.randrange(33, 531, 32)
        gridpos = (1+(pt1//32), 1+(pt2//32))

        while running:

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                #if there is a click on the mole, re-randomize position
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gridclicked = (event.pos[0]//32, event.pos[1]//32)
                    if gridpos == gridclicked:
                        pt1 = random.randrange(33, 659, 32)
                        pt2 = random.randrange(33, 531, 32)
                        gridpos = (1+(pt1//32), 1+(pt2//32))

            #draw BG and grid            
            screen.fill(darkGrey)
            for i in range(30, 682, 32):
                pygame.draw.line(screen, creme, (i, 30), (i, 542), 2)
            for j in range(30, 554, 32):
                pygame.draw.line(screen, creme, (30, j), (670, j), 2)

            #draw mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(pt1,pt2)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
